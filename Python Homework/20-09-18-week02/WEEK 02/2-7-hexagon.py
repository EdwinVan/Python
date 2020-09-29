# Hexagon画六角形
# 2020/09/18
# fyj

import turtle
import math
turtle.setup(1.0, 1.0, None, None)


# 画一条边，参数a为方向
def drawoneside(a):
    turtle.seth(a)
    turtle.fd(180)

# 第1个三角形
drawoneside(-90)
drawoneside(30)
drawoneside(150)

turtle.penup()
turtle.seth(-90)
turtle.fd(90)

turtle.seth(180)
b = 30 * math.tan(math.pi / 3) # 小知识：math库使用前需要导入，注意库中函数的用法
turtle.fd(b)

turtle.pendown()

# 第2个三角形
drawoneside(30)
drawoneside(-90)
drawoneside(150)


turtle.hideturtle()
