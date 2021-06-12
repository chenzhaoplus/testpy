import os
from multiprocessing import Queue
from multiprocessing import Process
import time


def task(q):
    try:
        print(os.getpid(), q.get())
        time.sleep(2)  # 模拟数据请求的耗时
    except Exception:
        return


if __name__ == '__main__':
    process_list = []  # 创建一个空列表用于存放进程对象
    q = Queue(10)  # 创建一个队列，容量为10
    for i in range(10):  # 模拟10个网址放入队列中
        url = f'www.{i}.com'
        q.put(url)
    start_time = time.time()
    for i in range(10):  # 创建10个子进程
        p = Process(target=task, args=(q,))  # 将task()作为任务函数、队列q作为参数传入子进程
        process_list.append(p)
        p.start()  # 由主进程开启子进程
    for p in process_list:
        p.join()  # 待每一个子进程都结束后再结束主进程
    print('程序耗时', time.time() - start_time)
    print('数据爬取完成')
