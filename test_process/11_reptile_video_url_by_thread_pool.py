import requests
import time
from lxml import etree
from concurrent.futures import ThreadPoolExecutor

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}


def get_response(url):  # 发起请求的函数
    response = requests.get(url=url, headers=headers)
    result = response.text
    html = etree.HTML(result)
    video_parse(html)  # 调用解析视频链接的函数


def video_parse(html):  # 解析视频链接的函数
    video_url = html.xpath('/html/body/div[2]/div[4]/ul/li/a[1]/div/video/@data-original')
    print(video_url)  # 打印视频链接


if __name__ == '__main__':
    poll = ThreadPoolExecutor(4)  # 创建容量为4的进程池
    start_time = time.time()  # 记录开始时间
    for i in range(1, 100):  # 创建网址队列
        url = f'http://699pic.com/video-sousuo-0-1-{i}-all-popular-0-0-0-0-0-0.html'
        poll.submit(get_response, url)  # 提交任务
    poll.shutdown(wait=True)
    finish_time = time.time()  # 记录结束时间
    pay_time = finish_time - start_time  # 计算耗时
    print(pay_time)
