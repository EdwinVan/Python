# 统计一行字符中不同类字符的个数 4-2.py
# fyj
# 2020/10/11

num_space = 0   # 空格数
num_letter = 0  # 字母数
num_num = 0     # 数字的数量
num_other = 0   # 其他字符

str = input("请输入一段字符串：")
for i in str:
    if i.isspace():
        num_space += 1
    elif i.isnumeric():
        num_num += 1
    elif 65<=ord(i)<=90 or 97<=ord(i)<=122:   # 通过unicode比较实现A~Z 65-90  a~z 97~122
        num_letter += 1
    else:
        num_other += 1
print("字母:{}  数字:{}  空格:{}  其他:{}".format(num_letter,num_num,num_space,num_other))




