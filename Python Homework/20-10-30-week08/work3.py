# 办公室分配
# 2020-10-30
# fyj

import random
offices = [[],[],[]]  # 定义一个列表来保存3个办公室

names = ['a','b','c','d','e','f','g','h']   # 定义一个列表来存储8位老师的名字


for name in names:  # 开始分配
    i = random.randint(0,2)
    offices[i].append(name)

# 输出分配结果
i = 1
for tempNames in offices:
    print("办公室{}中有{}个老师，分别是：".format(i,len(tempNames))),
    i += 1
    for name in tempNames:
        print("{}".format(name))
print("\n")




