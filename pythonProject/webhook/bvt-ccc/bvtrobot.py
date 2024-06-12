import json
import re
import subprocess
import time
import requests
import datetime

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

def send_post_request(url, data):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("POST请求发送成功！")
    else:
        print("POST请求发送失败！")

# 指定Webhook的URL
webhook_url = "https://xz.wps.cn/api/v1/webhook/send?key=d6cdac49fccab909ebf3c508c65618b7"


while 1:
    pachong()
    bvt = mo_bvt()
    print(bvt)
    if bvt!=None:
        break
    else:
        print('bvt未更新')
        time.sleep(60)

# Time = str(datetime.datetime.now()) # 获取电脑本机时间
content='今日bvt为:'+bvt[2:9]

# 要发送的数据
data = {
    "msgtype": "text",
    "text": {
        "content": content
    }
}

# 发送POST请求



# send_post_request(webhook_url, data)