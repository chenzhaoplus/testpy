from multiprocessing import Process
import time


class MyProcess(Process):  # 新建一个类，继承自Process类
    def __init__(self, name):
        super().__init__()  # 执行父类的构造函数
        self.name = name

    def run(self):  # 必须定义一个run()函数
        print(f'{self.name} 正在爬取')
        time.sleep(5)  # 模拟数据爬取需要的时间
        print(f'{self.name} 爬取完毕')


if __name__ == '__main__':  # Windows环境下，开启多进程的代码一定要写在这一行代码的下方
    p = MyProcess('www.1.com')
    p.start()  # 开启主进程
    print('主进程开始运行')
