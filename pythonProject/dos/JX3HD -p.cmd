@echo off
chcp 65001
set /p path=请输入客户端盘符 :
cd %path%:\client\interface\XAutoTest
WizardUltra.exe --JX3HD -p

pause
