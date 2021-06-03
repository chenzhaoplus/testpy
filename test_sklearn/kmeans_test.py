# 导入绘图库
import matplotlib.pyplot as plt
# 从Scikit-Learn库导入聚类模型中的K-means聚类算法
from sklearn.cluster import KMeans
# 导入聚类数据生成工具
from sklearn.datasets import make_blobs

# 用sklearn自带的make_blobs方法生成聚类测试数据
n_samples = 1500

# X 表示该聚类数据集共1500个样本，每个样本默认有2个特征值。y 表示这个1500个样本的“参考答案”的数据集
X, y = make_blobs(n_samples=n_samples)  # 默认 n_features=2，所以生成的 X shape 是 (n_samples,2)
print("X shape = ", X.shape)
print("y shape = ", y.shape)
print("y = ", y)
# plt.scatter(X[:, 0], X[:, 1], c=y)
# plt.show()

# 进行聚类，这里n_clusters设定为3，也即聚成3个簇
kmeans = KMeans(n_clusters=3)
clf = kmeans.fit(X)
y_pred = clf.predict(X)
# y_pred = kmeans.fit_predict(X)
print("y_pred shape = ", y_pred.shape)
print("y_pred = ", y_pred)

# 用点状图显示聚类效果
plt.scatter(X[:, 0], X[:, 1], c=y_pred)  # X[:, 0] 表示数组X第0列的所有数据; X[:, 1] 表示数组X第1列的所有数据
plt.show()
