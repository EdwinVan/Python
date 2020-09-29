# 蜷曲的蛇
# 2020/9/18
# fyj

import turtle
from turtle import *

turtle.setup(1.0 , 1.0 ,None ,None )
turtle.pendown()
turtle.pensize(25) 
turtle.seth(-40)

# the body of the python
for i in range(10):
    if i <= 5:
        turtle.circle(40 , 80)
        turtle.circle(-40, 80)
        left(45)
    elif i > 5 & i <= 6:
        turtle.circle(40 , 80)
        turtle.circle(-40, 80)
        left(65)
    elif i > 6 & i < 10:
        turtle.circle(40 , 80)
        turtle.circle(-40, 80)
        left(80)

        
# the head of the python
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
