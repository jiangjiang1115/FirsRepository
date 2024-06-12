import requests

url = 'http://10.11.146.212/getInfo.php?result=ok>'  # 替换为你要发送 GET 请求的 URL

response = requests.get(url)

if response.status_code == 200:
    print("get successful",response.content)
    # data = response.json()  # 如果返回的是 JSON 数据
    # print(data)
else:
    print('Failed to retrieve data:', response.status_code)