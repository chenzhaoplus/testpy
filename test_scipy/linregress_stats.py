import matplotlib.pyplot as plt
from scipy import stats

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x, y)


# y = slope * x + intercept
def myfunc(x):
    return slope * x + intercept


mymodel = list(map(myfunc, x))

# 绘制原始散点图
plt.scatter(x, y)

# 绘制线性回归线
plt.plot(x, mymodel)

plt.show()
