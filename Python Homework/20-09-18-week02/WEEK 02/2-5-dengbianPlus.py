# 2-5画叠加等边三角形
# 2020/09/18
# fyj

import turtle

turtle.setup(1.0, 1.0, None, None)
turtle.pendown()
turtle.fd(250) # 边长250

turtle.seth(120) 
turtle.fd(250) 

turtle.seth(-120)
turtle.fd(500)

turtle.seth(0)
turtle.fd(500)

turtle.seth(120)
turtle.fd(250)

turtle.seth(-120)
turtle.fd(250)

turtle.seth(120)
turtle.fd(250)

turtle.penup()

turtle.hideturtle() 
