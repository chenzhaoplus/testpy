import aiohttp
import asyncio
import time
from lxml import etree

'''
在asyncio模块中不能使用不支持异步的模块，这样会让异步的效果消失。因为requests模块不支持异步，所以这里使用aiohttp模块代替requests模块发起请求。
使用多任务异步协程时，在I/O阻塞操作的任务函数前需要添加await关键词，
例如，第18行和第9行代码的函数前就添加了await；同时还需要在第17行和第18代码中的每个with前添加async关键词，否则运行时会报错。
'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}


async def get_response(url):  # 发起请求的函数
    async with aiohttp.ClientSession() as s:
        async with await s.get(url=url, headers=headers) as response:
            result = await response.text()
            html = etree.HTML(result)
            return html


def video_parse(task):  # 解析视频链接的函数
    html = task.result()  # 取出任务函数的返回值，即获取到的网页源代码
    video_url = html.xpath('/html/body/div[2]/div[4]/ul/li/a[1]/div/video/@data-original')
    print(video_url)  # 打印视频链接


task_list = []
start_time = time.time()  # 记录开始时间
for i in range(1, 100):  # 创建网址队列
    url = f'http://699pic.com/video-sousuo-0-1-{i}-all-popular-0-0-0-0-0-0.html'
    coroutine = get_response(url)  # 实例化协程对象
    task = asyncio.ensure_future(coroutine)  # 封装任务对象
    task.add_done_callback(video_parse)  # 绑定回调函数
    task_list.append(task)  # 将任务对象添加到任务列表
loop = asyncio.get_event_loop()  # 创建事件循环对象
loop.run_until_complete(asyncio.wait(task_list))  # 开启事件循环对象
finish_time = time.time()  # 记录结束时间
pay_time = finish_time - start_time  # 计算耗时
print(pay_time)
