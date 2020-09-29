# 七彩同心圆 由外到内依次：红橙黄绿青蓝紫
# 20/9/19
# fyj

import turtle

a = 70
listcolor=["red" ,"orange", "yellow", "green" ,"cyan","blue","purple" ] #放入颜色名称
for i in range(7):
    turtle.fillcolor(listcolor[i])
    
    turtle.begin_fill()
    turtle.circle(a)
    turtle.penup()
    turtle.seth(90)
    turtle.fd(10)
    a-=10
    turtle.pendown()
    turtle.seth(0)
    turtle.end_fill()
turtle.hideturtle()
