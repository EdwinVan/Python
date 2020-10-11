# 4-6.py 验证羊车门更换选择是否会增加猜中汽车的机会
# fyj
# 2020/10/11

num_times = 100000
from random import *

def way_nochange():   # 不改变选择
    nochange_success = 0
    for times in range(num_times):
        list = ["sheep","sheep","sheep"]   # 初始化，每个门后都为羊
        num = randint(0,2)
        list[num] = "car"         # 1、2、3号门随机取一个放入car

        while True:
            # 第1次做出选择
            your_num1 = randint(0,2)
            your_num2 = your_num1
            # 揭晓选择结果
            # 猜对了
            if list[your_num2] == "car":
                nochange_success += 1
                break
            else:
                break
    a = nochange_success
    return a

def way_change():       # 改变选择
    change_success = 0
    for times in range(num_times):
        list = ["sheep", "sheep", "sheep"]  # 初始化，每个门后都为羊
        num = randint(0, 2)
        list[num] = "car"  # 1、2、3号门随机取一个放入car
        list2 = [" ", " ", " "]
        for i in range(len(list)):
            if list[i] != "car":
                list2[i] = list[i]
            else:
                list2[i] = " "
        list4 = [0, 0, 0]  # list4=[car_num,sheep_num1]
        while True:
            # 第1次做出选择
            your_num1 = randint(0, 2)
            # print("你第1次选择了{}号门".format(your_num1 + 1))
            for i in range(2):
                if list2[i] == "car":
                    car_num = i
                    list4[0] = car_num  # car所在索引位置，此门可能被参赛者选择

            # 第2次做出选择
            # 参赛者第一次选中的是车的门,改变选择，不获胜
            if your_num1 == list4[0]:
                break
            # 参赛者第一次选中的是羊的门
            else:
                change_success += 1
                break
    b = change_success
    return b


change_success = way_change()
nochange_success = way_nochange()

print("参赛者改变选择获胜了{}次".format(change_success))
print("参赛者坚持选择获胜了{}次".format(nochange_success))

print("改变选择的胜率：{:.2f}%".format(change_success/num_times*100))
print("坚持选择的胜率：{:.2f}%".format(nochange_success/num_times*100))

if change_success > nochange_success:
    print("改变选择增加了获胜机会")
else:
    print("改变选择不会增加获胜机会")