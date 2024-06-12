import os
import sys
import time
import json
import subprocess
import datetime
import requests

def kill_process(process_name):
    os.system("taskkill /f /im " + process_name)


process_name = "JX3ClientX64.exe"

# 关闭剑网三进程
kill_process(process_name)

def execute_command(command):
    # 打开cmd窗口并执行命令
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    # 读取命令执行结果
    if process.returncode == 0:
        result = output.decode('GB2312')
    else:
        result = error.decode('GB2312')
    return result

with open('config.json', 'r') as f:
    config = json.load(f)

# 你所要发布通知的机器人URL，根据需要修改
FEISHU_URL=config['FEISHU_URL']

class SvnOperator():

    def __init__(self) -> None:
        # 配置文件信息
        self.config_path = None # 配置文件路径
        self.ip = None # 测试机IP
        self.id = None # 测试机编号
        self.gpu = None # 测试机显卡
        self.path = None # 产品库存放目录
        self.revision = None # 产品库版本号（可选，默认最新）
        # 更新状态信息
        self.has_cleanup = False  # 是否已清除无版本控制的文件
        self.has_reverted = False  # 是否已恢复修改的文件
        self.has_updated = False  # 是否已更新成功

    def GetConfig(self) -> bool:
        #读取机器设备信息，和更新路径
        with open(self.config_path, 'r', encoding="utf-8") as f:
            config = json.load(f)
            self.ip = config.get("IP", None)
            self.id = config.get("ID", None)
            self.gpu = config.get("GPU", None)
            self.path = config.get("PATH", None)
            self.revision = config.get("REVISION", None)
        if self.path and isinstance(self.path, str) and os.path.exists(self.path): #判断路径是否存在
            return True
        else:
            print("[ERROR] Wrong path in the Config !")
            return False

    def GetSvnInfo(self):
        command = f"svn info {self.path}"   #获取文件svn信息
        print(f"---> {command}")
        try:
            info = execute_command(command)
            # print(info)
            if 'svn: E155007' in info:  # 说明此路径不是svn路径
                return None
            revision = info[info.find('Revision')+10 : info.find('\nNode')]  # 查找版本号字符串位置
            return revision
        except Exception as e:
            print(e)
            return None
#解锁
    def CleanUp(self) -> bool:
        command = f"svn cleanup {self.path}"
        print(f"---> {command}")
        try:
            subprocess.run(command, shell=True, check=True)
            return True
        except Exception as e:
            print(e)
            return False
#删除该工作副本中所有未版本控制或忽略的文件
    def CleanUpUnversioned(self) -> bool:
        command = f"svn cleanup --remove-unversioned {self.path}"
        print(f"---> {command}")
        try:
            subprocess.run(command, shell=True, check=True)
            self.has_cleanup = True
            return True
        except Exception as e:
            print(e)
            return False
#还原
    def Revert(self) -> bool:
        command = f"svn revert -R {self.path}"
        print(f"---> {command}")
        try:
            subprocess.run(command, shell=True, check=True)
            self.has_reverted = True
            return True
        except Exception as e:
            print(e)
            return False
#更最新
    def Update(self) -> bool:
        if self.revision:  #指定版本号更新
            command = f"svn update -r {self.revision} {self.path}"
        else:               #更最新
            command = f"svn update {self.path}"
        print(f"---> {command}")
        try:
            subprocess.run(command, shell=True, check=True)
            self.has_updated = True
            return True
        except Exception as e:
            print(e)
            return False

    def SendMsgToFeishu(self, last_revision):
        if not FEISHU_URL:
            print("[WARNING] Null url when send msg to Feishu !")
            return False
        headers = {
            "Content-Type": "application/json; charset=utf-8",
        }
        cur_time = datetime.datetime.now()
        if self.config_path:  # 适用于测试组
            content = f'SVN更新完成!\n' \
                    f'ID: {self.id}\n' \
                    f'IP: {self.ip}\n' \
                    f'显卡: {self.gpu}\n' \
                    f'路径: {self.path}\n' \
                    f'版本号: {last_revision}\n' \
                    f'时间: {cur_time}\n'
        else:
            content = f'SVN更新完成!\n' \
                    f'路径: {self.path}\n' \
                    f'版本号: {last_revision}\n' \
                    f'时间: {cur_time}\n'
        payload_message = {
            "msg_type": "text", # 表示消息类型为文本
            "content": { # 表示消息具体内容
                # @ 单个用户 <at user_id="ou_xxx">名字</at>
                # @ 所有人 <at user_id="all">所有人</at>
                "text": content
            }
        }
        try:
            response = requests.post(url=FEISHU_URL, data=json.dumps(payload_message), headers=headers)
            return response.json
        except Exception as e:
            print(e)
            return False

    def CheckArg(self, argv) -> bool:
        # Model-1 : python SvnUpdate.py -f config_path
        # Model-2 : python SvnUpdate.py path revision
        if len(argv) < 2:
            print("[ERROR] Too Less Args !")
            return False
        if isinstance(argv[1], str) and argv[1] == "-f":  # match Model-1
            if len(sys.argv) > 2 and isinstance(argv[2], str) and os.path.exists(argv[2]):
                self.config_path = argv[2]
                return self.GetConfig()
            else:
                print("[ERROR] Wrong Args !")
                return False
        elif isinstance(argv[1], str) and os.path.exists(argv[1]):  # match Model-2
            self.path = argv[1]
            if len(sys.argv) > 2 and isinstance(sys.argv[2], str) and sys.argv[2].isdigit():
                self.revision = int(sys.argv[2])
            return True
        else:
            print("[ERROR] Wrong Args !")
            return False

    def Dispatch(self) -> None:
        if self.GetSvnInfo() is None:
            print("[ERROR] The path is not SVN product !!!")
            return
        while self.has_updated is not True:
            self.CleanUp()
            #if not self.has_cleanup:
            #    self.CleanUpUnversioned()
            if not self.has_reverted:
                self.Revert()
            self.Update()
        self.SendMsgToFeishu(self.GetSvnInfo())

SHENDU_PATH=config["SHENDU_PATH"]
# 将指定路径设置为深度函数就不会 更新这个目录
def ShenDu():
    try:
        # 指定路径
        path = SHENDU_PATH

        # 指定cmd指令
        cmd = 'svn up --set-depth empty '+path

        # 在指定路径下执行cmd指令
        os.chdir(path)
        os.system(cmd)
    except:
        print('无')


if __name__ == "__main__":
    ShenDu()
    print(sys.argv)
    o = SvnOperator()
    if o.CheckArg(sys.argv):
        o.Dispatch()
    print("Task Done !")