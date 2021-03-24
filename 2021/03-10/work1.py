# 程序编写 测试三角形类型识别程序的BUG
# fyj
# 2021-3-10

# txt中每行第一个字母含义：
# a代表不规则三角形
# b代表等腰三角形
# c代表等边三角形
# d代表不能构成三角形
# e代表不符合输入标准

import math


def main():
    with open('num.txt', 'r') as f:
        data = f.readlines()
        for i in data:
            i = i.strip()
            num = i.split(" ")
            if len(num) != 4:    # 正常情况为：1个预期值+3条边
                for i in range(len(num)-1):
                    print("{:<5}".format(num[i+1]), end="")
                print("       ", end="")
                print("{:<12}".format("不能构成三角形"), end="")
                if num[0] == 'd':
                    print("{:>9}".format("Correct"))
                else:
                    print("{:>9}".format("Wrong"))
            else:
                expect = num[0]       # expect为每行数据的第一个字母，代表预期输出值
                edge1 = eval(num[1])  # 第一条边
                edge2 = eval(num[2])  # 第二条边
                edge3 = eval(num[3])  # 第三条边

            print("{:<5}{:<5}{:<5}".format(edge1, edge2, edge3), end="  ")
            test(expect, edge1, edge2, edge3)


# 判断三角形类型
def test(expect, a, b, c):
    if a <= 0 or b <= 0 or c <= 0:  # 三条边长存在小于等于0的数 不能构成三角形
        print("{:<12}".format("不能构成三角形"), end="")
        if expect == 'd':
            print("{:>9}".format("Correct"))
        else:
            print("{:>9}".format("Wrong"))

    elif '.' in str(a) or '.' in str(b) or '.' in str(c):  # 边长含小数 不符合输入要求
        print("{:<12}".format("边长存在小数"), end="")
        if expect == 'e':
            print("{:>9}".format("Correct"))
        else:
            print("{:>9}".format("Wrong"))

    elif math.pow(a, 2)+math.pow(b, 2) < math.pow(c, 2) or math.pow(a, 2)+math.pow(c, 2) < math.pow(b, 2) or math.pow(b, 2)+math.pow(c, 2) < math.pow(a, 2):  # 任意两边平方和小于第三边 不能构成三角形
        print("{:<12}".format("不能构成三角形"), end="")
        if expect == 'd':
            print("{:>9}".format("Correct"))
        else:
            print("{:>9}".format("Wrong"))

    elif (a == b or a == c or b == c) and (a != c or a != b or b != c):  # 仅存在两条边同样长
        print("{0:<12}".format("等腰三角形"), end="")
        if expect == 'b':
            print("{:>9}".format("Correct"))
        else:
            print("{:>9}".format("Wrong"))

    elif a == b and a == c:      # 三条边同样长
        print("{:<12}".format("等边三角形"), end="")
        if expect == 'c':
            print("{:>9}".format("Correct"))
        else:
            print("{:>9}".format("Wrong"))
    else:
        print("{:<12}".format("不规则三角形"), end="")
        if expect == 'a':
            print("{:>9}".format("Correct"))
        else:
            print("{:>9}".format("Wrong"))


main()
