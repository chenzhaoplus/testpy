import pandas as pd
import numpy as np

"""
参考： https://blog.csdn.net/xtfge0915/article/details/52938740
"""

# ------------------------- 利用字典创建一个DataFrame ----------------------------
data = {"one": np.random.randn(4), "two": np.linspace(1, 4, 4), "three": ['zhangsan', '李四', 999, 0.1]}
df = pd.DataFrame(data, index=[1, 2, 3, 4])
# print(df)


# ------------------------- 设置索引 -------------------------
df = df.set_index(['one', 'two'])
# print(df)


# ------------------------- 利用数组创建一个DataFrame -------------------------
data = np.random.randn(6, 4)  # 创建一个6行4列的数组
df = pd.DataFrame(data, columns=list('ABCD'), index=[1, 2, 'a', 'b', '2006-10-1', '第六行'])
# print(df)
# print(df.A)  # 按列读取
# print(df[['A', 'B']])  # 按列读取, df['列名']or df[['列名']]、df[['列名1','列名2','列名n']]
# print(type(df['A']))
# print(type(df[['A']]))  # df['A']和 df[['A']]都能读取第一列数据，但它们的返回结果是不同的
print(df.iloc[:1, :])  # 读取第一行
# print(df.iloc[:, :1])  # 读取第一列
# print(df.iloc[:, 1:3])  # 读取第1列到第3列
# print(df.iloc[:, 2:])  # 读取第2列之后的数据
# print(df.iloc[:, :3])  # 读取前3列数据

# ------------------------- 创建一个空的DataFrame -------------------------
df = pd.DataFrame(columns=('id', 'name', 'grade', 'class'))
# print(df)
