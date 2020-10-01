# 同心圆
# 20/9/19
# fyj

import turtle

a = 10
listcolor=["red" ,"orange", "yellow", "green","blue" ,"cyan","purple" ] #放入颜色名称
list=listcolor[::-1]
for i in range(8):
    turtle.fillcolor(list[i])
    turtle.begin_fill()
    turtle.circle(a)
    turtle.penup()
    turtle.seth(-90)
    turtle.fd(10)
    a+=10
    turtle.pendown()
    turtle.seth(0)
    turtle.end_fill()
    
