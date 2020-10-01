# 画一个彩色同心圆
# fyj
# 2020/09/20

import turtle
turtle.circle(50)
turtle.seth(90)
turtle.fd(10)
turtle.circle(40)

r = 100
for i in range(7):
    turtle.circle(r)
    r -= 10
    
