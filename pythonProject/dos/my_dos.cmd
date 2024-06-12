@echo off
chcp 65001
echo.
echo.
echo.
echo.
::C:\Users\admin\Desktop\xx.xls
::start c:abc.txt
::start http://iqb.testplus.cn:5003/#%E9%A1%B9%E7%9B%AE%E5%B7%A5%E5%85%B7
::md 要完整路径   创建文件夹，修改服务器
start http://jx3ops.xsjom.com/common/bvt_version_info/
rem 注释信息的rem,上条为打开网址
::taskkill /F /IM Code.exe :: /F强制杀进程 , /IM 进程名
::set /p path=请输入客户端盘符 :   rem 建变量path，获取输入的变量值
::echo %path%  rem 打印变量用两个%%
::echo XSkillPoint | clip  rem复制并打印内容
::type 123.txt | clip 打印文档的内存，先cd到文档路径，再用type
exit
pause