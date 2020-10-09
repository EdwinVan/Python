# 设计一个自己的logo
# fyj
# 2020-10-09

import turtle
turtle.pendown()
turtle.pensize(3)
a = 35
listcolor = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]  # 放入颜色名称
for i in range(7):
    turtle.fillcolor(listcolor[i])

    turtle.begin_fill()
    turtle.circle(a)
    turtle.penup()
    turtle.seth(90)
    turtle.fd(5)
    a -= 5
    turtle.pendown()
    turtle.seth(0)
    turtle.end_fill()

# 外圈大圆
turtle.seth(-90)
turtle.pensize(4)
turtle.penup()
turtle.fd(95)
turtle.pendown()
turtle.seth(0)
turtle.circle(100)

turtle.pensize(3)
# 下黑
turtle.fillcolor("black")
turtle.begin_fill()
turtle.penup()
turtle.seth(90)
turtle.fd(30)
turtle.pendown()
turtle.circle(-5,180)
turtle.circle(-10,180)
turtle.seth(-90)
turtle.circle(5,180)
turtle.end_fill()


turtle.penup()
turtle.seth(90)
turtle.fd(130)

# 上黑
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(-5,180)
turtle.seth(90)
turtle.circle(10,180)
turtle.circle(5,180)
turtle.end_fill()


turtle.penup()
turtle.seth(-90)
turtle.fd(65)
turtle.seth(0)
turtle.fd(65)

# 右黑
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(-5,180)
turtle.seth(0)
turtle.circle(10,180)
turtle.circle(5,180)
turtle.end_fill()


turtle.penup()
turtle.seth(-180)
turtle.fd(130)

# 左黑
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(-5,180)
turtle.seth(-180)
turtle.circle(10,180)
turtle.circle(5,180)
turtle.end_fill()

turtle.hideturtle()
