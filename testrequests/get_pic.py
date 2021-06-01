# 获取图片

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}

url = 'http://test.smcaiot.com/M00/26/16/rBAE1l6WqlmAXNCdAABPA5tDsaU.232e56'

response = requests.get(url=url)

content = response.content

with open('图片.jpg', 'wb') as fp:
    fp.write(content)
