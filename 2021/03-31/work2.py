import pandas as pd

data = pd.Series({'讲座': 70, '演出': 15, '科技赛': 82, '会议': 20, '球赛': 8})
print("1 创建对象存储信息")
print(data)

add = pd.Series({'论坛': 12})
data = data.append(add)
print("\n2 增加活动" )
print(data)

data['演出'] = 18
print("\n3 修改演出值为18" )
print(data)

print("\n4 输出后三行数据")
print(data.tail(3))

print("\n5 次数大于20的活动如下")
for i in range(data.size):
    if data.values[i] > 20:
        print("{}  {}".format(data.index[i],data.values[i]))

print("\n6 删除球赛的数据")
del data['球赛']
print(data)
print("\n程序结束")

