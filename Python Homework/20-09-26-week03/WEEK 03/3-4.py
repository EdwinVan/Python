# 3.4 回文数字判断
# fyj

num = input("请输入一个5位数字: ")
if num[0] == num[4]:
    if num[1] == num[3]:
        print("{}是一个回文数字".format(int(num)))
    else:
        print("{}不是一个回文数字".format(int(num)))
else:
    print("{}不是一个回文数字".format(int(num)))