import asyncio
import time


async def get_page(url):  # 使用async关键词修饰函数，使函数在被调用时返回一个协程对象
    print(f'正在爬取{url}')
    await asyncio.sleep(1)
    print(f'{url}爬取完毕')


url_list = ['www.1.com', 'www.2.com', 'www.3.com', 'www.4.com', 'www.5.com']  # 网址列表
task_list = []  # 任务对象列表
for url in url_list:
    coroutine = get_page(url)  # 实例化一个协程对象
    task = asyncio.ensure_future(coroutine)  # 将协程对象封装为任务对象
    task_list.append(task)  # 将任务对象存放到列表中
loop = asyncio.get_event_loop()  # 创建一个事件循环对象
time1 = time.time()
loop.run_until_complete(asyncio.wait(task_list))  # 将任务对象列表中的任务对象逐个注册到事件循环对象中
time2 = time.time() - time1
print(time2)  # 查看任务运行耗时
