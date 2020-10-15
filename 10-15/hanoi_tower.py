# 实现汉诺塔的算法,并打印步骤
# 2020/10/15
# fyj


times = 0

def hanoi(n,A,B,C):
    global times
    if(n==1):
        print(A,"-->",C,end="   ")
        times = times + 1
        print(times)
    else:
        hanoi(n-1,A,C,B)
        print(A,"-->",C,end="   ")
        times = times + 1
        print(times)
        hanoi(n-1,B,A,C)

n = eval(input("请输出圆盘数量n= "))
hanoi(n,'A','B','C')

