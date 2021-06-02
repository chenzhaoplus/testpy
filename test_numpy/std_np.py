# 计算标准差，意味着大多数值在平均值的 0.9 范围内，即 86.4 的正负 0.9 范围内
import numpy

speed = [86, 87, 88, 86, 87, 85, 86]

mean_value = numpy.mean(speed)
print("平均值：", mean_value)

x = numpy.std(speed)

print("标准差：", x)
