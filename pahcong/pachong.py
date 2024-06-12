import json
import re
import subprocess
import time
import requests
import datetime
import os
import signal

import psutil
def pachong():
    # 定义要爬取的页面URL
    response = requests.get("http://jx3ops.xsjom.com/common/bvt_version_info/")

    # 检查响应状态码
    if response.status_code == 200:
        # 获取响应内容
        content = response.text

        with open("baidu.txt", "w", encoding="utf-8") as file:
            file.write(content)

    else:
        print("请求失败，状态码：", response.status_code)

def extract_numbers_from_string(string):
    numbers = re.findall(r'\d+', string)
    return numbers


def mo_bvt():
    with open('baidu.txt', 'rb') as f:
        data = f.read()
    a1=str(data)

    bytes_text = a1.encode('utf-8')


    # end_index = a1.find('<td>2023-09-06 10:02:32</td>')  379290
    end_index = a1.find('</tbody>')
    end_index2 = a1.find('<td>1241305</td>')

    # a3爬的是时间
    a3=a1[end_index-157:end_index-147]
    print(a3)
    string = a3

    ssss = str(string)
    print(ssss)
    a4 = datetime.datetime.now()  # 获取电脑本机时间
    a4z=str(a4)

    if ssss in a4z:
        # a4爬的是bvt号
        a4 = a1[end_index - 270:end_index - 170]
        string = a4
        # print(string)
        numbers = extract_numbers_from_string(string)
        my_list = numbers
        my_tuple = set(my_list)
        my_set = my_tuple
        # my_string就是当天bvt号
        my_string = str(my_set)
        print('bvt已更新',my_string)
        return my_string
    else:
        print('BVT还未更新')
a=1

class FeishuTalk:
    # 发送文本消息
    with open('pak.json', 'r') as f:
        config = json.load(f)
        chatGPT_url = config['chatGPT_url']
    def sendTextmessage(self, content):
        url = self.chatGPT_url
        headers = {
            "Content-Type": "application/json; charset=utf-8",
        }
        payload_message = {
            # 表示消息类型为文本
            "msg_type": "text",
            # 表示消息具体内容
            "content": {
                # @ 单个用户 <at user_id="ou_xxx">名字</at>
                # "text":"<at user_id='all'>\"bf888888\">test</at>"+content
                "text":content
                # @ 所有人 <at user_id="all">所有人</at>
                # "text": content + "<at user_id=\"all\">test</at>"
            }
        }
        # json.dumps将方法转为json格式
        response = requests.post(url=url, data=json.dumps(payload_message), headers=headers)
        return response.json

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
def update(bvt_int):
    # 读取pak文件里的动态数据
    with open('pak.json', 'r') as f:
        config = json.load(f)
    command = config['command']
    print(command)
    print(config)
    output = execute_command(command)   #svn信息
    # 输出返回结果
    print(output)

    a6 = config['a6']
    c=config['c']
    c2=' '
    c4='client'

    bvt11=c+c2+bvt_int+c2+c4
    print('bvt=',bvt)

    FeishuTalk().sendTextmessage(f'{a6}正在执行update至版本:{bvt_int}')
    # # 升级至指定版本
    result = execute_command(bvt11)
    FeishuTalk().sendTextmessage(f'{a6}已更新至今日的bvt:{bvt_int}')
    print('execute_command result:', result)


# 读取pak文件里的动态数据
with open('pak.json', 'r') as f:
    config = json.load(f)
command = config['command']
print(command)
print(config)
output = execute_command(command)
# 输出返回结果
print(output)
# 将获取的客户端信息写入
with open('a1.txt', 'w+') as f:
    f.write(output)
time.sleep(2)
# 读取刚写入的客户端信息
with open('a1.txt')as f:
    data=f.read()
a2=data.find('Revision')#查找版本号字符串位置
a3=data[a2+9:a2+17]#将字符串切片，切出版本号

print('客户端版本为',a3)

sleep=int(config['sleep'])
print(f'等待时间为{sleep}s')


# 杀死进程代码
def kill_process(process_name):
    os.system("taskkill /f /im " + process_name)

# 杀掉内存
process_name = "JX3ClientX64.exe"
kill_process(process_name)

# 查找自动更新程序是否存在
def judgeprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            print(pid)
            return pid
            break
    else:
        print("not found")


ji=1

# 此循环在循环查找svn更新程序是否存在
while ji:
    a111=judgeprocess('SvnUpdate.exe')
    print('a==============',a111)
    if a111!=None:
        print('★★★★★正在等待更新,请勿关闭★★★★★')
        time.sleep(100)
    else:
        print('★★★★★更新开始★★★★★')
        break
b=1

while a:
    pachong()
    time.sleep(2)
    mo_bvt()
    bvt = mo_bvt()
    bvt1 = bvt
    bvt_str = str(bvt1).replace('{', '').replace('}', '')
    bvt_str2 = str(bvt_str).replace("'", "").replace("'", "")
    print('今天的bvt=', type(bvt_str2))
    print('bvt_str2=', bvt_str2)
    b+=1
    if b>100:
        break

    if isinstance(bvt_str2, int) or isinstance(bvt_str2, str) and len(bvt_str2) > 5:
        # 如果版本不匹配 则更新
        print('a3===',type(a3))
        print('bvt_str2===', type(bvt_str2))
        if bvt_str2 in a3:
            print('客户端版本为',a3)
            print(f'已更新至版本{bvt_str2}')
            break
        else:
            print('客户端版本为', a3)
            print('客户端版本不相等')
            update(bvt_str2)
            break
    else:
        # 在bvt_str2为None或其他类型时执行的操作
        print('bvt_str2不是一个数字')
        time.sleep(sleep)
