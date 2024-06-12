import ctypes
import sys
import os

# 搜索当前目录及其子目录下的指定文件路径
# 指定目录下找
def find_file_path(filename,path=r"d:\\"):
    for root, dirs, files in os.walk(path):
        if filename in files:
            full_path=os.path.join(root, filename)
            cd_path=full_path.replace(filename,'')
            return full_path
    return None

# 盘符+：\
# path_root=input("请输入盘符：")+":\\"
import PySimpleGUI as sg

sg.theme('DarkBlue3')  # 设置主题
sg.theme_background_color('#444444')  # 设置背景颜色
sg.set_options(font=('Arial', 12))  # 设置字体样式

layout = [[sg.Text('输入盘符:',background_color='#444444',text_color="#ddd"), sg.Input(background_color='#333333',text_color="#ffffff",key='-ARGS-',size=(10)),
          sg.Button('Enter',button_color=('white', 'grey'),size=(4,1))]]

window = sg.Window('Input Something',layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Enter':
        break

path_root = values['-ARGS-'].split()
print("Arguments:", path_root)
window.close()

filename = 'WizardHD.exe'
result = find_file_path(filename,path_root[0]+":\\")
# 输出第一个找到的文件
if result:
    print(f'文件 {filename} 的路径是：{result}')
else:
    print(f'未找到文件 {filename}')

# 写入批处理
def create_file_with_extension(file_name,result):
    with open(file_name, 'w') as file:
        # 可选：写入一些内容到文件中
        file.write(f'''@echo on
{result[0:2]} 
cd {result.replace(filename,'')}
{filename} "-p"
exit
pause
''')

# 使用示例
file_name = r'd:\my_dos.cmd'
create_file_with_extension(file_name,result)

# 以管理员身份打开命令提示符
# 运行批处理（写入指定目录和程序）
def open_cmd_as_admin_and_execute_command(command):
    ctypes.windll.shell32.ShellExecuteW(None, "runas", r"d:\my_dos.cmd", "/k " , None, 1)
command =file_name  # 替换为你想执行的具体命令
print(command)
open_cmd_as_admin_and_execute_command(command)
# os.remove(file_name)

sys.exit()