# 获取网页源代码
import json

import requests

headers = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
    "token": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxNjI1MDM1MTE0MTA0IiwiaWF0IjoxNjI1MDM1MTE0LCJzdWIiOiJtYW5hZ2UiLCJpc3MiOiJhZG1pbiIsImV4cCI6MTYyNzYyNzExNH0.zRRDRNd-iLJPGX00ksTnx1gNGrm3hXbWYEgkP3okKq4"
}

url = 'http://172.16.4.84/smcaiot-aggregation/api/v1/datamonitor/findWorkOrderPageList'

data = {
    "pageNum": 1,
    "pageSize": 10,
    "startTime": "2021-06-01 00:00:00",
    "endTime": "2021-07-01 00:00:00",
    "orderStatuses": ["4"]
}

response = requests.post(url=url, headers=headers, data=json.dumps(data))

print(response.text)
