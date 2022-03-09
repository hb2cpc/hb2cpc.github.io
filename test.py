
#-*-coding:GBK -*-

import requests
import base64
import json
'''
公式识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/formula"
# 二进制方式打开图片文件
f = open('img.png', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '24.a18ae24fb76a13f7294ea846128b87ad.2592000.1648653167.282335-25681045'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())