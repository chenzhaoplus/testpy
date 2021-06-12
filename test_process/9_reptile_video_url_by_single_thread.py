import requests
import time
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
url_list = []  # 网址列表
for i in range(1, 100):  # 在网址列表中添加网址
    url = f'http://699pic.com/video-sousuo-0-1-{i}-all-popular-0-0-0-0-0-0.html'
    url_list.append(url)


def get_response(url):  # 发起请求的函数
    response = requests.get(url=url, headers=headers).text
    html = etree.HTML(response)
    video_parse(html)  # 调用解析视频链接的函数


def video_parse(html):  # 解析视频链接的函数
    video_url = html.xpath('/html/body/div[2]/div[4]/ul/li/a[1]/div/video/@data-original')
    print(video_url)  # 打印视频链接


start_time = time.time()  # 记录开始时间
for url in url_list:
    get_response(url)
finish_time = time.time()  # 记录结束时间
pay_time = finish_time - start_time  # 计算耗时
print(pay_time)
