# 猜字游戏 4-5.py
# fyj
# 2020/10/11

from random import *

num = randint(0,100)           # 用random库随机产生一个0-100的数字作为预设数字
last_num = 0                   # 用户预测次数初始化为0

print("提示：位于0-100的整数")
while True:
    try:
        your_num = input("请输入数字：")
        your_num = eval(your_num)
        if isinstance(your_num,int):
            last_num += 1
            if your_num == num:
                print("预测{}次，你猜中了！".format(last_num))
                break
            elif not (0 <= your_num <= 100):
                print("请输入一个0-100的整数！")
            else:
                if your_num > num:
                    print("遗憾太大了")
                else:
                    print("遗憾太小了")
        else:
            print("输入内容必须为整数！")
    except NameError:
        print("输入内容必须为整数！")
