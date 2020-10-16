# 5-3.py 判断一个字符串是否为整数、浮点数或复数
# 2020/10/16
# fyj

def isNum(str):
    if type(str)== int or type(str)== float or type(str)== complex :
        return True
    else:
        return False

def main():
    str = eval(input("请输入一段字符串: "))
    while(isNum(str)==True):
        print("属于整数、浮点数、复数")
        break

    while(isNum(str)==False):
        print("不属于整数、浮点数、复数")
        break

main()