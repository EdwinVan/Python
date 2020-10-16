# 5-1.py 画一个大的田字格
# 2020/10/16
# fyj

def drawstr1():
    print("+----+----+----+----+")

def drawstr2():
    print("|    |    |    |    |")

def drawmatts():
    for i in range(21):
        if i in [0,5,10,15,20]:
            drawstr1()
        else:
            drawstr2()

def main():
    drawmatts()

main()
