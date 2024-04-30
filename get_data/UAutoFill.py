import csv
import requests
import traceback
import win32file,os
import sys
import json
#封装伪装浏览器层,请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44',
    'Referer' : 'http://perfeye.console.testplus.cn/case/list?appKey=mecha',
    "Authorization": "Bearer mj6cltF&!L#yWX8k"}

def GetWorkPath():
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    return application_path 

workPath = GetWorkPath()   

# 获取各项数据
class Reoprt():
    def __init__(self,ReportUrl = "",ID = ""):
        self.report_info = ReopertInfo()        #获取的数据项
        if ReportUrl != "":
            listUrl = ReportUrl.split('/')
            if len(listUrl)>1:      #获取uuid
                uuid = listUrl[4]
            else:
                uuid = listUrl[0]
            self.REPORTURL = ReportUrl
            self.APIURL = "http://perfeye.console.testplus.cn/api/show/task/" + uuid            
        elif ID != "":
            self.REPORTURL = f"http://perfeye.console.testplus.cn/case/{ID}/report"
            self.APIURL = "http://perfeye.console.testplus.cn/api/show/task/" + ID
        else:
            return 0

    def get_reportInfo(self):
        try:
            res = requests.post(self.APIURL, headers=headers)
            if res.ok:
                res=res.json()
                self.report_info.read_json(res,self.REPORTURL)
            else:
                if res.status_code == 401:
                    print("cookie失效，请更换")
                else:
                    # print("输入的url有误，请重新输入----")
                    print(f"未知异常： {res}")
        except:
            print("失败了")
            traceback.print_exc()
        
class ReopertInfo():
    def __init__(self):
        self.device_name = ""
        self.casename = ""
        self.AppVersion = ""
        self.REPORTURL = ""
        self.DataList = ""

        self.__AllLabelInfo = ""
        self.__OtherLabelInfo = ""

    def read_json(self,res,ReportUrl):
        # writefile(res, os.path.join(workPath, "1.json"))    # 写入到json方便找数据
        if res.get("message") == "\u975e\u516c\u5f00\u7684\u62a5\u544a":
            print(f"非公开的报告: {ReportUrl}")
            return False
        self.REPORTURL = ReportUrl.replace('\n','')
        self.device_name = res['data']['BaseInfo']["DeviceModel"].split("(")[0]
        self.casename = res['data']['BaseInfo']['CaseName']
        self.AppVersion = res['data']['BaseInfo']['AppVersion'].split(".")[0]
        self.res = res

        self.__AllLabelInfo = res['data']["LabelInfo"]["All"]
        self.__OtherLabelInfo = res['data']["LabelInfo"]["Other"]

    def get_AllLabeInfo(self):   #获取的数据
        if self.__AllLabelInfo != "":
            dateitme = self.__AllLabelInfo
            label=dateitme['Name']
            DetailFPS = dateitme['LabelFPS']
            DetailCpu = dateitme['LabelCPU']
            DetailGpu = dateitme['LabelGPU']
            DetailMemory = dateitme['LabelMemory']
            DetailRender = dateitme['LabelRenderer']
            AvgDrawTriangles = dateitme["LabelRenderer"]["Avg(DrawTriangles)"]    # Avg(DrawTriangles)
            MaxDrawTriangles = dateitme["LabelRenderer"]["Max(DrawTriangles)"]    # Max(DrawTriangles)
            AvgDrawcall = dateitme["LabelRenderer"]["Avg(Drawcall)"]         # Avg(Drawcall)
            MaxDrawcall = dateitme["LabelRenderer"]["Max(Drawcall)"]         # Max(Drawcall)

            avgfps = DetailFPS['AvgFPS']
            maxfps = DetailFPS['MaxFPS']
            minfps = DetailFPS['MinFPS']
            tp90fps = DetailFPS['TP90']
            Smoothness = DetailFPS['Smoothness(%)']
            Jank = DetailFPS['Jank(/10min)'] 
            BigJank = DetailFPS['BigJank(/10min)'] 

            avgapp = DetailCpu['AvgApp(%)']
            maxapp = DetailCpu['MaxApp(%)']
            AvgTotalCPU = DetailCpu['AvgTotal(%)']
            MaxCTemp = DetailCpu['MaxCTemp']    # cpu温度max
            AvgCTemp = DetailCpu['AvgCTemp']    # cpu温度avg

            InitMemory = DetailMemory['InitMemory(MB)']
            AvgMemory = DetailMemory['AvgMemory(MB)']
            PeakMemory = DetailMemory['PeakMemory(MB)']
            AvgSwapMemory = DetailMemory['AvgSwapMemory(MB)']
            PeakSwapMemory = DetailMemory['PeakSwapMemory(MB)']

            avgGpuLoad = DetailGpu['Avg(GPULoad)[%]']
            maxGpuLoad = DetailGpu['Max(GPULoad)[%]']
            avgGpuMemry = DetailGpu['Avg(GPUMemoryUsed)[MB]']
            maxGpuMemry = DetailGpu['Peak(GPUMemoryUsed)[MB]']

            avgDrawcall = DetailRender['Avg(Drawcall)']
            maxDrawcall = DetailRender['Peak(Drawcall)']                   
            avgVertex = DetailRender['Avg(Vertex)']
            maxVertex = DetailRender['Peak(Vertex)']

            AppVersion = self.res['data']['BaseInfo']['AppVersion']   # 版本号
            Duration = self.res['data']['BaseInfo']['Duration'].replace(' ','')    # 案例时长
            MaxBTemp = dateitme["LabelBTemp"]["PeakBTemp"]    # Max(BTemp)[℃]

            # print(f"{self.casename} {self.AppVersion} {self.device_name} {avgfps} {tp90fps} {Jank} {BigJank} {DetailCpu['App<=60(%)']} {PeakMemory} {Smoothness} {self.REPORTURL}")   # Tgame用 
            # print(f"{avgfps} {minfps} {tp90fps} {Smoothness} {AvgTotalCPU} {avgapp} {AvgMemory} {PeakMemory} {AvgSwapMemory} {PeakSwapMemory}")      # Xgame单项屏蔽用
            print(f"{self.casename} {self.device_name} {avgfps} {maxfps} {minfps} {tp90fps} {Jank} {BigJank} {AvgMemory} {InitMemory} {PeakMemory} {AvgDrawTriangles} {MaxDrawTriangles} {AvgDrawcall} {MaxDrawcall} {Duration} {self.REPORTURL}")      # Xgame场景跑图用（GI用）
            # print(f"{avgfps} {tp90fps} {PeakMemory} {AvgCTemp} {MaxCTemp} {MaxBTemp} {Jank} {BigJank} {Smoothness} {self.REPORTURL} ")      # Xgame视频组件用
            # print(f"{self.casename} {self.device_name} {avgfps} {tp90fps} {Jank} {BigJank} {Smoothness} {self.REPORTURL}")   # 通用
            # print(f"{avgfps} {minfps} {tp90fps} {Smoothness} {AvgTotalCPU} {avgapp} {AvgMemory} {PeakMemory} {AvgSwapMemory} {PeakSwapMemory} {self.REPORTURL}")   # Xgame植被采集用
            #返回需要的数据
            return self.casename,'','',avgfps,'','','','','',minfps,tp90fps,avgapp,PeakMemory,'','',avgGpuLoad,avgGpuMemry,self.REPORTURL



    def get_OtherLabeInfo(self):
        if self.__OtherLabelInfo != "":
            datalen = len(self.__OtherLabelInfo)
            for dateitme in self.__OtherLabelInfo:       
                label=dateitme['Name']
                if datalen>1 and( "战斗" not in label ):
                    # print("跳过数据",casename,label)
                    continue
                DetailFPS = dateitme['LabelFPS']
                DetailCpu = dateitme['LabelCPU']
                DetailGpu = dateitme['LabelGPU']
                DetailMemory = dateitme['LabelMemory']
                DetailRender = dateitme['LabelRenderer']

                avgfps = DetailFPS['AvgFPS']
                maxfps = DetailFPS['MaxFPS']
                minfps = DetailFPS['MinFPS']
                tp90fps = DetailFPS['TP90']
                Smoothness = DetailFPS['Smoothness(%)']
                Jank = DetailFPS['Jank(/10min)'] 
                BigJank = DetailFPS['BigJank(/10min)'] 

                avgapp = DetailCpu['AvgApp(%)']
                maxapp = DetailCpu['MaxApp(%)']

                InitMemory = DetailMemory['InitMemory(MB)']
                AvgMemory = DetailMemory['AvgMemory(MB)']
                PeakMemory = DetailMemory['PeakMemory(MB)']

                avgGpuLoad = DetailGpu['Avg(GPULoad)[%]']
                maxGpuLoad = DetailGpu['Max(GPULoad)[%]']
                avgGpuMemry = DetailGpu['Avg(GPUMemoryUsed)[MB]']
                maxGpuMemry = DetailGpu['Peak(GPUMemoryUsed)[MB]']

                avgDrawcall = DetailRender['Avg(Drawcall)']
                maxDrawcall = DetailRender['Peak(Drawcall)']                   
                avgVertex = DetailRender['Avg(Vertex)']
                maxVertex = DetailRender['Peak(Vertex)']

                print(f"{label} {self.AppVersion} {self.device_name} {avgfps} {tp90fps} {Jank} {BigJank} {DetailCpu['App<=60(%)']} {PeakMemory} {Smoothness} {self.REPORTURL}")

class ReopertList():
    def __init__(self):
        self.CustomizeHeaders = {"mysession":"MTY3NjQzODkwN3xOd3dBTkZWTlIwVlpURWxJV1ROS05VMU9OMVZDVWsxVVMxQklWVFJaUnpOVVZrTTJSRmRSVUZSWFVrVTBVVWRKTlZSSk0xVkdNMUU9fAnMOCiJoEDs9EU7KWtYAE4XUdetHgtROL93L_8fCUdL", "project_key":"tgame"}
        self.configPath = os.path.join(workPath,"ListConfig.json")
        with open(self.configPath,'r',encoding="UTF-8") as file:
            self.config = json.load(file)

    def select_UAutoReport(self):
        api_url = self.config["UAuto"]["url"]
        parameter_json = self.config["UAuto"]["parameter_json"]
        res = requests.post(api_url, json= parameter_json,headers=headers)
        rjson = res.json()
        data = rjson['data']
        print(f"获取数据{len(data)}/{rjson['total']}")
        for report in data:
            DeviceName = report['DeviceName']
            if "PCKM00" in DeviceName or "Mi_10" in DeviceName or  "HRY_AL00Ta" in DeviceName:
                reportID = report['ID']
                report = Reoprt(ID = reportID)
                report.get_reportInfo()
                report.report_info.get_OtherLabeInfo()

    def select_CustomizeUAutoReport(self):
        api_url = self.config["customizeUAuto"]["url"]
        parameter_json = self.config["customizeUAuto"]["parameter_json"]
        res = requests.post(api_url, json= parameter_json,headers=headers)
        rjson = res.json()
        data = rjson['data']
        print(f"获取数据{len(data)}/{rjson['total']}")
        for report in data:
            Scenes = report['Scenes']
            if "资源更新" in Scenes:
                continue
            reportID = report['ID']
            report = Reoprt(ID = reportID)
            report.get_reportInfo()
            report.report_info.get_AllLabeInfo()

    def select_Customize(self):
        api_url = self.config["customize"]["url"]
        parameter_json = self.config["customize"]["parameter_json"]
        res = requests.post(api_url, json= parameter_json,headers=self.CustomizeHeaders)
        print(res.text)
        rjson = res.json()
        data = rjson['data']
        print(f"获取数据{len(data)}/{rjson['total']}")
        for report in data[::-1]:
            reportID = report['ID']
            #self.set_Shared(reportID)
            report = Reoprt(ID = reportID)
            report.get_reportInfo()
            report.report_info.get_AllLabeInfo()


    def set_Shared(self,reportID):
        url = "http://perfeye.console.testplus.cn/api/share/task/" + reportID
        parameter_json = {
            "TaskID": "reportID",
            "IsShared": True,
            "IsPrivateShare": False,
            "Password": "",
            "ExpireTime": 0
        }
        res = requests.post(url, json= parameter_json,headers=self.CustomizeHeaders)
        rjson = res.json()
        print(rjson)


def is_used(file_name):
	try:
		vHandle = win32file.CreateFile(file_name, win32file.GENERIC_READ, 0, None, win32file.OPEN_EXISTING, win32file.FILE_ATTRIBUTE_NORMAL, None)
		return int(vHandle) == win32file.INVALID_HANDLE_VALUE
	except:
		return True
	finally:
		try:
			win32file.CloseHandle(vHandle)
		except:
			pass


# 将resq写入文件
def writefile(res, file):
    with open(file, 'w') as f:
        json.dump(res, f)


# 读取config文件，获取数据链接，可循环放入列表获取各个指标数据
def read_report_config():
    workPath = GetWorkPath()
    configFilePath = os.path.join(workPath,"config.txt")
    # with open(configFilePath,'r',encoding="UTF-8") as file:   #获取单报告链接
    #     return file.readlines()
    with open(configFilePath, 'r', encoding="UTF-8") as clinks:  #处理对比链接
        AllLinks=clinks.read()
        link=AllLinks.split('/')[4][:-11].split(',')
        for i in range(len(link)):
            link[i]='https://perfeye.console.testplus.cn/case/'+link[i]+'/report?appKey=JX3'
        # print(link)
        return link

def read_repotlist_config():
    workPath = GetWorkPath()
    configFilePath = os.path.join(workPath,"ListConfig.json")
    with open(configFilePath,'r',encoding="UTF-8") as file:
        return json.load(file)



def write_ToFile(resultData,filename):
    if filename==None or filename==""or filename=="None":
        filename=f'./result.csv'
    else:
        filename=f'./{filename}.csv'
    if os.path.isfile(filename):
        while is_used(filename):
            finput("{filename} 文件被占用 请关闭打开的文件- 关闭后回车继续")

    with open(filename,"w",newline='',encoding="utf-8") as f:
        writer = csv.DictWriter(f, ["用例","画质","场景","AvgFPS","AvgFPS差值","AvgFPS差值占比","MS","MS差值","MS差值占比","MinFPS","FPS TP90","AvgAppCPU(%)",
                 "PeakMemory(MB)","虚拟峰值差值","虚拟峰值差值占比","Avg(GPULoad)[%]","Avg(GPUMemoryUsed)[MB]","报告链接"])  #标头,第一行数据
        writer.writeheader()
        for row in range(len(resultData)):
            print("输出数据:",resultData[row])
            writer.writerow(resultData[row])



ppdatalist=[ ]

def select_reoprtList(api_url, parameter_json): 
    
    res = requests.post(api_url, json= parameter_json,headers=headers)
    rjson = res.json()
    data = rjson['data']
    print(f"获取数据{len(data)}/{rjson['total']}")
    # for 
    
def main():
    ppdatalist = read_report_config()
    # rl = ReopertList()
    # #rl.select_CustomizeUAutoReport()
    # rl.select_Customize()

    resultData=list(range(len(ppdatalist)))
    resIndex=0
    for dataitme in ppdatalist:  #循环获取链接
        report = Reoprt(dataitme)
        report.get_reportInfo()
        dataKey=["用例","画质","场景","AvgFPS","AvgFPS差值","AvgFPS差值占比","MS","MS差值","MS差值占比","MinFPS","FPS TP90","AvgAppCPU(%)",
                 "PeakMemory(MB)","虚拟峰值差值","虚拟峰值差值占比","Avg(GPULoad)[%]","Avg(GPUMemoryUsed)[MB]","报告链接"]
        dataValue=report.report_info.get_AllLabeInfo()
        dataDic={}
        for i in range(len(dataKey)):
            dataDic[dataKey[i]]=dataValue[i]
        resultData[resIndex]=dataDic
        resIndex+=1

    task_name='res'
    write_ToFile(resultData,task_name)
    #print(f"{task_name}数据加入完成")

if __name__ == "__main__":
#     reoprts_url = "http://perfeye.console.testplus.cn/api/show/project"
#     parameter_json = {
#   "AppKey": "tgame",
#   "OSType": "android",
#   "DoUpload": "true",
#   "Scenes": [
#     "稳定性测试(珠海自动化(雷家丰))"
#   ],
#   "StartTime": "2023-02-20 00:00:51",
#   "EndTime": "2023-02-26 23:59:02",
#   "From": 0,
#   "Size": 100
# }
#     select_reoprt(reoprts_url,parameter_json)
    main()
            
        