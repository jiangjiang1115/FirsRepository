import time

import requests
from datetime import datetime
import re
import json
def get_bvt():
    while 1:
        content = str(requests.get("http://jx3ops.xsjom.com/common/bvt_version_info/").content)
        nowTime=str(datetime.now().date()) #当天日期
        fine_time="<td>"+nowTime
        fine_index=content.find(fine_time) #查找
        if fine_index==-1:
            print("bvt未更新...")
            time.sleep(10)
            continue
        else:
            find_bvt=content[fine_index-161:fine_index+170]
            bvt_send_time=content[fine_index+4:fine_index+23]
            print(bvt_send_time)
            get_number=re.findall(r'\d+', find_bvt)
            bvt=get_number[0]
            break
    msg="今日bvt："+bvt+"\n"
    print(msg)
    data={
        "msgtype":"card",
            "card":{
                "header": {
                    "title": {
                        "tag": "text",
                        "content": {
                            "type": "plainText",
                            "text": "剑网三-重制"
                        }
                    },
                    "template": "yellow"
                },
                "elements": [
                        {
                            "tag": "hr",
                            "style": "dashed"
                        },
                        {
                            "tag": "text",
                            "content": {
                                "type": "markdown",
                                "text": "#####  今日bvt："+bvt+
                                        "\n\n>"+bvt_send_time
                            },

                        }
                    ]
            }
    }
    return data

# 机器人url
webhook_url="https://xz.wps.cn/api/v1/webhook/send?key=d6cdac49fccab909ebf3c508c65618b7"

# 获取对应IP的资源版本号
#请求体
def get_serverinfo(ip):
    json_data={"serverIP":ip}
    respond=requests.post("http://iqb.testplus.cn:8008/api/v1/getServerInfo",json=json_data)
    server=json.loads(respond.content)["result"]
    print(server)
    serverinfo={
            "msgtype":"card",
            "card":{
                "header": {
                    "title": {
                        "tag": "text",
                        "content": {
                            "type": "plainText",
                            "text": "重制-稳定性服务器"
                        }
                    },
                    "template": "yellow"
                },
                "elements": [
                        {
                            "tag": "hr",
                            "style": "dashed"
                        },
                        {
                            "tag": "text",
                            "content": {
                                "type": "markdown",
                                "text": "######  服务器地址:10.11.68.174\n"+
                                    "\n######  <font color=''>资源版本号:</font>"+server["resVersion"]+
                                     "\n\n######  当前版本号："+server["serverVersion"]+
                                     "\n\n######  运行状态："+server["state"]
                            },

                        }
                    ]
                }
    }
    return serverinfo


def send_xiezuo(webhook_url,data):
    response1 = requests.post(webhook_url, json=data)
    print(response1.status_code)

data=get_bvt()
serverinfo174=get_serverinfo("10.11.68.174")
send_xiezuo(webhook_url,data)
send_xiezuo(webhook_url,serverinfo174)

