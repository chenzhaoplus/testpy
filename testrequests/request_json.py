import requests
import json
import testscipy as tsc

url = 'http://172.16.4.84/smcaiot-basicinfo/basicperson/list?order=desc&sort=id&pageNum=1&pageSize=10&mobileNumber=&name=&communityId=&buildingId=&unitId=&floorId=&roomId='

params = {}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}

resp = requests.get(url=url, params=params, headers=headers)

content = resp.json()

# print(json.dumps(content, indent=4, separators=(',', ':')))

print(json.dumps(content['data'], indent=4, separators=(',', ':')))

# for i in content:
#     print(json.dumps(i, indent=4, ensure_ascii=False, separators=(',', ':')))
#     break  # 只打印第一条