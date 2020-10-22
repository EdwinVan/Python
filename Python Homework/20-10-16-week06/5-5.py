# 判断一个整数是否是素数
# 2020/10/21
# fyj

import math

def IsPrime(num):
    times = 0
    if num <= 0:
        print("请输入一个正整数")
        return False
    elif num == 1:
        return True
    elif num > 1:
        for i in range(num+1):
            if i > 1 and num % i == 0:
                times += 1
        if times <= 1:
            return True
        else:
            return False

def main():

    num = eval(input("请输入一个正整数: "))
    if IsPrime(num) == True:
        print("{}是素数\n".format(num))
    else:
        print("{}不是素数\n".format(num))

main()