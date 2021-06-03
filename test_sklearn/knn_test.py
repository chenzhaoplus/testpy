from sklearn.datasets import load_iris
# 从Scikit-Learn库导入近邻模型中的KNN分类算法
from sklearn.neighbors import KNeighborsClassifier

# 载入鸢尾花数据集
X, y = load_iris(return_X_y=True)
print("X shape = ", X.shape)
print("y shape = ", y.shape)
print("y = ", y)

# 训练模型
clf = KNeighborsClassifier().fit(X, y)  # knn分类算法是有监督算法，所以需要y这个“参考答案”做拟合
# 使用模型进行分类预测
predict = clf.predict(X)
print("predict shape = ", predict.shape)
print("predict = ", predict)

print("性能评分 = ", clf.score(X, y))
