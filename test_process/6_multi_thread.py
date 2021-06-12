from threading import Thread
import time
import random


def task(url_list):
    try:
        print(random.choice(url_list))
        time.sleep(2)  # 模拟数据请求的耗时
    except Exception:
        return


if __name__ == '__main__':
    thread_list = []  # 创建一个空列表用于存放线程对象
    url_list = []  # 创建一个空列表用于存放所有网址
    for i in range(10):  # 模拟10个网址放入列表中
        url = f'www.{i}.com'
        url_list.append(url)
    start_time = time.time()
    for i in range(10):  # 创建10个子线程
        t = Thread(target=task, args=(url_list,))  # 将task()作为任务函数，队列q作为参数传入子线程
        thread_list.append(t)
        t.start()  # 由主线程开启子线程
    for t in thread_list:
        t.join()  # 待每一个子线程都结束后再结束主进程
    print('程序耗时', time.time() - start_time)
    print('数据爬取完成')
