import ctypes
import os
import sys


def run_as_admin(command):
    """
    以管理员方式运行 CMD
    """
    # 调用 Windows API ShellExecute
    ctypes.windll.shell32.ShellExecuteW(None, "runas", command, None, None, 1)

# # 测试运行 CMD，，打开路径用字符串
run_as_admin("cmd.exe")
# 管理员cmd
# ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", None, None, 1)
#打开能够以管理员身份运行的文件
# ctypes.windll.shell32.ShellExecuteW(None, "runas", r"C:\Users\admin\AppData\Local\Kingsoft\WPS Office\ksolaunch.exe", None, None, 1)
print("打开")
#找路径，打开程序，指定盘符？

# import os
#
# # 搜索当前目录及其子目录下的指定文件路径
# # 指定目录下找
# def find_file_path(filename,path=r"d:"):
#     for root, dirs, files in os.walk(path):
#         if filename in files:
#             full_path=os.path.join(root, filename)
#             cd_path=full_path.replace(filename,'')
#             return full_path
#     return None
#
# # 盘符+：
# path_root=input("请输入盘符：")
# filename = 'WizardHD.exe'
# result = find_file_path(filename,path_root)
# # 输出第一个找到的文件
# if result:
#     print(f'文件 {filename} 的路径是：{result}')
# else:
#     print(f'未找到文件 {filename}')
#
# # 写入批处理
# def create_file_with_extension(file_name,result):
#     with open(file_name, 'w') as file:
#         # 可选：写入一些内容到文件中
#         file.write(f'''@echo on
# {result[0:2]}
# cd {result.replace(filename,'')}
# {filename} "-p"
# exit
# pause
# ''')
#
# # 使用示例
# file_name = r'C:\Users\admin\Desktop\my_dos.cmd'
# create_file_with_extension(file_name,result)
#
# # 以管理员身份打开命令提示符
# # 运行批处理（写入指定目录和程序）
# def open_cmd_as_admin_and_execute_command(command):
#     # 使用ctypes调用ShellExecute函数
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", "/K " + command, None, 1)
#
# command =file_name  # 替换为你想执行的具体命令
# print(command)
# open_cmd_as_admin_and_execute_command(command)
# sys.exit()

