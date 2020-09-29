# Cornerless square 画无角正方形
# 2020/09/18
# fyj

import turtle
turtle.setup(1.0, 1.0, None, None)

def drawoneside(): # 此函数用以实现画一条边
    turtle.penup()
    turtle.fd(70)
    turtle.pendown()
    turtle.fd(210)
    turtle.penup()
    turtle.fd(70)

drawoneside()

turtle.seth(90)
drawoneside()

turtle.seth(180)
drawoneside()

turtle.seth(-90)
drawoneside()

turtle.hideturtle() 
