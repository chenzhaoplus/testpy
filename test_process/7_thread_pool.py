from concurrent.futures import ThreadPoolExecutor
from threading import current_thread, Lock
import time

a = 1
lock = Lock()


def task(url1):
    lock.acquire()  # 加锁
    time.sleep(1)  # 模拟I/O阻塞
    global a
    print(f'线程{current_thread().ident}开始第{a}个任务')  # 使用current_thread().ident查看线程ID
    a += 1
    lock.release()  # 解锁


executor = ThreadPoolExecutor(max_workers=3)  # 创建线程池
for i in range(1, 11):
    future = executor.submit(task, i)  # 创建子线程并获取返回值
executor.shutdown()  # 关闭线程池
