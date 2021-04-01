import pandas as pd
from pandas import DataFrame
import numpy as np

print("1 创建数据如下")
data = {"one": [1, 2, 3],
        "two": [4, 5, 6],
        "three": [7, 8, 9]
        }
data = DataFrame(data, index=['a', 'b', 'c'])
print(data)


print("\n2 查询列索引为two和three两列数据")
print(data[['two', 'three']])


print("\n3 第0行、第2行、第0列、第2列数据")
print(data.loc['a'])
print(data.loc['b'])
print(data['one'])
print(data['two'])


print("\n4 筛选第1列中值大于2的所有行数据，另存为data1对象")
data1 = data[(data['one'] > 2)]
data1 = DataFrame(data1)
print(data1)


print("\n5 为data1添加一列数据，列索引为four，值都为10")
data1.insert(data1.shape[1], 'four', 10)
print(data1)


print("\n6 将data1所有值大于9的数据修改为8")
data1[data1 > 9] = 8
print(data1)


print("\n7 删除data1中第0行数据")
data1 = data1.drop(['c'], axis=0)  # axis=0表示按行索引删除
print(data1)
print("\n程序结束")