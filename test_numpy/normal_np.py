# 典型的正态数据分布
import numpy
import matplotlib.pyplot as plt

# 指定平均值为 5.0，标准差为 1.0。这意味着这些值应集中在 5.0 左右，并且很少与平均值偏离 1.0。
x = numpy.random.normal(5.0, 1.0, 100000)

# 绘制具有 100 栏的直方图
plt.hist(x, 100)
plt.show()
