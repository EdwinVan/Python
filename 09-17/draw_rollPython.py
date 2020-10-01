# Draw a roll python一坨蛇
# 2020/9/17
# fyj

import turtle
turtle.setup(1.0 , 1.0 ,None ,None ) # 创建一个画板

turtle.pendown()
turtle.pencolor("green")
turtle.pensize(25) # 设置画笔大小


# the body of the python
turtle.circle(150,270)
turtle.circle(120,250)
turtle.circle(90,250)
turtle.circle(60,270)

# the head of the python
turtle.seth(10) 
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
