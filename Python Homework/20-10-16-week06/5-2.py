# 5-2 写一个函数，判断整数是奇数还是偶数
# 2020/10/16
# fyj

def isOdd(n):
    if n % 2 == 0:
        print("{}是偶数".format(n))
    else:
        print("{}是奇数".format(n))

def main():
    n = eval(input("请输入一个整数: "))
    isOdd(n)

main()