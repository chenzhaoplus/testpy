# 创建一个包含 250 个介于 0 到 5 之间的随机浮点数的数组：
import numpy

x = numpy.random.uniform(0.0, 5.0, 250)
print(x)

# 绘制直方图
import matplotlib.pyplot as plt

plt.hist(x, 5)
plt.show()
