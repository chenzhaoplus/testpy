import matplotlib.pyplot as plt
import numpy as np

# 生成由30个元素组成的二位数据集，区间在-3至3之间
x = np.linspace(-3, 3, 30)
y = 2 * x + 1

# print("old x = ", x)
# print("old y = ", y)

# 数据集绘图
# plt.scatter(x, y)
# plt.show()

from sklearn import linear_model

# 将数组改成矩阵
x = [[i] for i in x]
y = [[i] for i in y]

# print("x = ", x)
# print("y = ", y)

# 训练线性回归模型
model = linear_model.LinearRegression()
model.fit(x, y)

# 为了检验训练的结果，提供一组测试用的x_
x_ = [[1], [2]]
# 进行预测
predict = model.predict(x_)
print(predict)
