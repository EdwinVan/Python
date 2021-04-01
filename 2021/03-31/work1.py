# Date:2021-3-31
# Au:FYJ
# 考察：数组的使用
# “天天”、“家乐”、“联华”和“农工”四个超市都卖苹果、香蕉、桔子和芒果四种水果
# 使用NumPy创建一维和二维数组对象，管理超市水果价格


import numpy as np
import random

# 第1问
market = np.array(["天天", "家乐", "联华", "农工"])
fruit = np.array(["苹果", "香蕉", "桔子", "芒果"])

# 第2问
a = np.zeros((4, 4))  # 值全为0的4*4数组
for i in range(4):
    for j in range(4):
        a[i][j] = random.randint(4, 10)
price = np.array(a)
print(" 各超市的水果价格如下\n", price)

# 第3问
first = 0
second = 0
for m in range(market.size):
    if market[m] == "天天":
        first = m
for n in range(fruit.size):
    if fruit[n] == "苹果":
        second = n

price[first][second] += 1
print("\n 天天的苹果价格增加1元\n", price)

# 第4问
first_2 = 0
for a in range(market.size):
    if market[a] == "农工":
        first_2 = a

for b in range(fruit.size):
    price[first_2][b] -= 2

print("\n 农工的所有水果价格减少2元\n", price)

average_price = [0, 0, 0, 0]  # list保存水果平均价格，默认为0
for i in range(fruit.size):
    price_demo = 0
    for j in range(market.size):
        price_demo += price[j][i]

    average_price[i] = price_demo / market.size # 每一类水果的平均价格

print("\n 各类水果平均价格如下")
print(fruit)
print(average_price)

# 第6问
pos_orange = 0
for i in range(fruit.size):
    if fruit[i] == "桔子":
        pos_orange = i

expensive_Orange = price[0][pos_orange]  # 默认第一家店的桔子最贵
pos_market = 0
for j in range(market.size):
    if price[j][pos_orange] > expensive_Orange:
        expensive_Orange = price[j][pos_orange]  # 找最贵的桔子，输出商店相关数据
        pos_market = j

print("\n 桔子最贵的超市名称 {}".format(market[pos_market]))
print("\n程序结束")