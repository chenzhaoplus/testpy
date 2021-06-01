# 计算方差：指示值的分散程度
# 实际上，如果采用方差的平方根，则会得到标准差！
# 或反之，如果将标准偏差乘以自身，则会得到方差！
import numpy

speed = [86, 87, 88, 86, 87, 85, 86]

x = numpy.var(speed)

print(x)
