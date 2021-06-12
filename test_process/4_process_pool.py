import os
import time
from multiprocessing.pool import Pool  # 导入Pool类创建进程池


def task(i):  # 定义任务函数
    print(f'{os.getpid()}处理第{i}个任务')
    time.sleep(2)


if __name__ == '__main__':
    poll = Pool(4)  # 创建容量为4的进程池，最多创建4个进程
    for i in range(1, 11):
        poll.apply_async(task, (i,))  # 异步提交任务
    poll.close()  # 关闭进程池
    poll.join()  # 使用异步方式提交任务，必须使用close()和join()函数，目的是等待进程池的子进程结束后才结束主进程，并关闭进程池
