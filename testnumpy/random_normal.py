# 创建两个数组，它们都填充有来自正态数据分布的 1000 个随机数。
# 第一个数组的平均值设置为 5.0，标准差为 1.0。
# 第二个数组的平均值设置为 10.0，标准差为 2.0：
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()
