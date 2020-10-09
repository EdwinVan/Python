# 画一朵玫瑰花
# fyj
# 2020-10-09

import turtle

turtle.penup()
turtle.seth(-90)
turtle.fd(150)
turtle.seth(0)
"""
# left
turtle.pendown()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(60,180)
turtle.circle(-100,180)
turtle.seth(-180)
turtle.circle(160,180)

# right
turtle.seth(-180)
turtle.circle(-60,180)
turtle.circle(100,180)
turtle.seth(0)
turtle.circle(-160,180)
turtle.end_fill()
"""

turtle.pendown()
turtle.seth(-90)
turtle.fd(250)
turtle.fd(-100)
turtle.seth(0)
for i in range(20):
    turtle.seth(5)
    turtle.fd(5)

for i in range(20):
    turtle.seth(-5)
    turtle.fd(-5)
