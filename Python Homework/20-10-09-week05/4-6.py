# 4-6.py 验证羊车门更换选择是否会增加猜中汽车的机会demo
# fyj
# 2020/10/11

num_times = 100000
from random import *
nochange_success = 0
change_success = 0
nochange_loser = 0
change_loser = 0



for times in range(num_times):
    print("**********{}**********".format(times+1))
    list = ["sheep","sheep","sheep"]   # 初始化，每个门后都为羊
    num = randint(0,2)
    list[num] = "car"         # 1、2、3号门随机取一个放入car
    list2 = [" "," "," "]
    for i in range(len(list)):
        if list[i] != "car":
            list2[i] = list[i]
        else:
            list2[i] = " "

    print(list)
    list4 = [0,0,0]        # list4=[car_num,sheep_num1]
    list5 = [0,0,0]        # list5=[sheep_num2,num_2]
    while True:

        # 第1次做出选择
        your_num1 = randint(0,2)
        print("你第1次选择了{}号门".format(your_num1+1))
        for i in range(2):
            if list2[i] == "car":
                car_num = i
                list4[0] = car_num    # car所在索引位置，此门可能被参赛者选择

        # 第2次做出选择
        # 参赛者第一次选中的是车的门
        if your_num1 == list4[0]:
            for i in range(2):
                if list[i] != "car" and i != your_num1:
                    print("主持人提示你：{}号门后是羊".format(i + 1))  # sheep_num1为主持人所开门后露出的小羊，此门参赛者不会再选
                    sheep_num1 = i
                    list4[1]= sheep_num1
                    for m in range(2):
                        if m not in list4:
                            sheep_num2 = m  # sheep_num2为没有被主持人开门露出的小羊，此门可能被参赛者选择
                            list5[0] = sheep_num2
                    break

            list3 = [your_num1,list5[0]]  # 第一次选择的门（后面是车）、除主持人所开门之外的另一个门（后面是另一只羊）
            for i in range(2):
                num_2 = list3[randint(0, 1)]  # 从主持人所开门后的另外两扇门随机选择一扇
                list5[1] = num_2
                break
            your_num2 = list5[1]

        # 参赛者第一次选中的是羊的门
        else:
            for i in range(2):
                if list[i] != "car" and i != your_num1:
                    print("主持人提示你：{}号门后是羊".format(i + 1))  # sheep_num1为主持人所开门后露出的小羊，此门参赛者不会再选
                    sheep_num1 = i
                    list4 += [sheep_num1]
                    for m in range(2):
                        if m not in list4:
                            sheep_num2 = m  # sheep_num2为没有被主持人开门露出的小羊，此门可能被参赛者选择
                            list5[0] = sheep_num2
                    break

            list3 = [your_num1, list5[0]]  # 第一次选择的门（后面是羊）、除主持人所开门之外的另一个门（后面是车）
            for i in range(2):
                select = randint(0, 1)    # 从上面两个门中随机选择一个门
                num_2 = list3[select]  # 从主持人所开门后的另外两扇门随机选择一扇
                list5[1] = num_2
                break
            your_num2 = list5[1]



        # 揭晓选择结果
        print("你第2次选择了{}号门".format(your_num2+1))
        if list[your_num2] == "car":
            if your_num2 == your_num1:
                print("你坚定了你的选择，你猜对了！".format(your_num2+1))
                nochange_success += 1
                break
            else:
                print("你改变了你的选择，你猜对了！".format(your_num2 + 1))
                change_success += 1
                break
        else:
            if your_num2 == your_num1:
                print("你坚定了你的选择，你猜错了！".format(your_num2 + 1))
                nochange_loser += 1
                break
            else:
                print("你改变了你的选择，你猜错了！".format(your_num2 + 1))
                change_loser += 1
                break

print("循环执行了{}次，总结如下：".format(num_times))
print("参赛者改变选择获胜了{}次".format(change_success))
print("参赛者坚持选择获胜了{}次".format(nochange_success))
print("参赛者改变选择失败了{}次".format(change_loser))
print("参赛者坚持选择失败了{}次".format(nochange_loser))
print("改变选择的胜率：{}".format())
print("坚持选择的胜率：{}".format())