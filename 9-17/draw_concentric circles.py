# draw concentric circles同心圆
# 20/09/17
# fyj

import turtle
turtle.setup(1.0 , 1.0 ,None , None)

turtle.pendown()
turtle.pensize(5)
turtle.circle(150)

turtle.penup()
turtle.seth(90)
turtle.fd(30)
turtle.seth(0)
turtle.pendown()
turtle.circle(120)

turtle.penup()
turtle.seth(90)
turtle.fd(30)
turtle.seth(0)
turtle.pendown()
turtle.circle(90)

turtle.penup()
turtle.seth(90)
turtle.fd(30)
turtle.seth(0)
turtle.pendown()
turtle.circle(60)

turtle.penup()
turtle.seth(90)
turtle.fd(30)
turtle.seth(0)
turtle.pendown()
turtle.circle(30)

turtle.penup()
turtle.seth(90)
turtle.fd(30)
turtle.seth(0)
turtle.pendown()
turtle.circle(2)

turtle.hideturtle() # 隐去turtle
