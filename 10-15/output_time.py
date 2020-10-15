# 使用七段码打印当前系统的时间(年、月、日、时、分、秒)
# 2020/10/15
# fyj

import turtle, datetime

def drawGap():  # 画一段空格
    turtle.penup()
    turtle.fd(5)
    turtle.pendown()

def drawLine(draw):                                  # 画七段数码管的其中一条线
    drawGap()                                        # 画空格
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)                                    # 七段数码管中一段的长度
    drawGap()
    turtle.right(90)

def drawDigit(d):                                    # 绘制一个数字
    turtle.pendown()
    drawLine(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 6, 8] else drawLine(False)

    turtle.left(90)

    drawLine(True) if d in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 2, 3, 4, 6, 7, 8, 9] else drawLine(False)

    turtle.penup()                       # 为下一个数字绘制做准备
    turtle.seth(0)
    turtle.fd(20)

def drawLetter(l):                      # 绘制一个字母
    turtle.pendown()
    drawLine(True) if l in "FY" else drawLine(False)
    drawLine(True) if l in "YJ" else drawLine(False)
    drawLine(True) if l in "YJ" else drawLine(False)
    drawLine(True) if l in "F" else drawLine(False)
    turtle.left(90)
    drawLine(True) if l in "FY" else drawLine(False)
    drawLine(True) if l in "F" else drawLine(False)
    drawLine(True) if l in "YJ" else drawLine(False)

    turtle.penup()
    turtle.seth(0)
    turtle.fd(20)

def drawDate(date):
    for i in date:
        if i == '-':
            turtle.fd(40)
        else:
            drawDigit(eval(i))

def drawName(name):
    for i in name:
        drawLetter(i)

def main():
    turtle.setup(1.0, 1.0, None, None)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    timenow = datetime.datetime.now().strftime("%Y-%m-%d")  # 获取当前时间
    drawDate(timenow)  # 打印时间

    turtle.penup()
    turtle.seth(-90)
    turtle.fd(160)
    # turtle.seth(-180)
    # turtle.fd(270)
    turtle.seth(0)
    turtle.fd(-220)
    turtle.pendown()

    drawName("FYJ")  # 打印名字
main()
