import json

import requests


class FeishuTalk:
    # 应用凭证，获取方式查看上面的步骤
    app_id = "cli_a37c6ffbdxxxxxxx"
    app_secret = "mLstZkv0C4d1sxxxxxxxxxxxxxxx"
    # 机器人webhook
    chatGPT_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/XXX'

    def __init__(self):
        # 获取tenant_access_token，供上传图片接口使用
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        headers = {
            "Content-Type": "application/json; charset=utf-8",
        }
        payload_data = {
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }
        response = requests.post(url=url, data=json.dumps(payload_data), headers=headers).json()
        self.token = response['tenant_access_token']

    # 发送图片
    def uploadImage(self, picturePath):
        image_key_headers = {
            'Authorization': 'Bearer ' + self.token,
        }
        # 上传图片获取image_key
        get_image_key_url = "https://open.feishu.cn/open-apis/im/v1/images"
        form = {'image_type': 'message',
                'image': (open(picturePath, 'rb'))}  # 需要替换具体的path
        multi_form = MultipartEncoder(form)
        image_key_headers['Content-Type'] = multi_form.content_type
        response = requests.request("POST", get_image_key_url, headers=image_key_headers, data=multi_form).json()
        # print(response.headers['X-Tt-Logid'])  # for debug or oncall
        image_key = response['data']['image_key']
        print("image_key：", image_key)
        # 发送图片
        url = self.chatGPT_url
        form = {'msg_type': 'image',
                'content':
                    {"image_key": image_key}
                }
        headers = {
            'Authorization': 'Bearer ' + self.token
        }
        response = requests.post(url=url, data=json.dumps(form), headers=headers)
        return response.json()


# 发送图片消息
picturePath = "E:\PythonCodes\FeishuTalk\picLibs\1.jpg"
FeishuTalk().uploadImage(picturePath)
