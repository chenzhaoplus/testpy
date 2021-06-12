from multiprocessing import Process
import time


def task(url1):  # 执行爬虫任务的函数
    print(f'{url1} 正在爬取')
    time.sleep(5)
    print(f'{url1} 爬取完毕')


if __name__ == '__main__':  # Windows环境下，开启多进程的代码一定要写在这一行代码的下方
    p = Process(target=task, kwargs={'url1': 'www.1.com'})  # 用参数target传入执行爬虫任务的函数task()，其参数url1的值用参数kwargs以字典格式传入
    p.start()  # 开启主进程，通知操作系统在内存中开辟一个空间，将p进程放进去由CPU执行
    print('主进程开始运行')
