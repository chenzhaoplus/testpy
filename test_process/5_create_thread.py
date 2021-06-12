from threading import Thread


def task(url1):  # 模拟爬虫任务
    print(f'{url1}正在爬取')


if __name__ == '__main__':
    t = Thread(target=task, args=('www.1.com',))  # 创建线程
    t.start()  # 开启主线程
    print('主线程开始')
