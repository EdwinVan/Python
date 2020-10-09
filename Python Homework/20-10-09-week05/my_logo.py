# 设计一个logo
# fyj

import turtle
turtle.pendown()

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
turtle.penup()
turtle.fd(95)
turtle.pendown()
turtle.seth(0)
turtle.circle(100)

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
turtle.seth(-90)
turtle.fd(30)
turtle.seth(90)
turtle.fd(160)

# 上黑
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(-5,180)
turtle.seth(90)
turtle.circle(10,180)
turtle.circle(5,180)
turtle.end_fill()