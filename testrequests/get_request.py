# 获取网页源代码

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}

url = 'http://172.16.4.84/smcaiot-basicinfo/basicperson/list?order=desc&sort=id&pageNum=1&pageSize=10&mobileNumber=&name=&communityId=&buildingId=&unitId=&floorId=&roomId='

params = {}

response = requests.get(url=url, headers=headers, params=params)

print(response.json())
