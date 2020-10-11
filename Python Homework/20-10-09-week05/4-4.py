# 猜字游戏 4-4.py
# fyj
# 2020/10/11

from random import *

num = randint(0,100)           # 用random库随机产生一个0-100的数字作为预设数字
last_num = 0                   # 用户预测次数初始化为0

print("提示：位于0-100的整数")

while(True):
    your_num = eval(input("请输入数字："))
    last_num += 1
    if your_num == num :
        print("预测{}次，你猜中了！".format(last_num))
        break
    elif not (0<=your_num<=100) :
        print("请输入一个0-9的整数！")
    else:
        if your_num > num:
            print("遗憾太大了")
        else:
            print("遗憾太小了")