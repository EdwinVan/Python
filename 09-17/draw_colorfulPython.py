# Draw a colorful python七彩蛇
# 2020/9/17
# fyj

import turtle
turtle.setup(1.0 , 1.0 ,None ,None ) # 创建一个画板
turtle.penup()
turtle.fd(-450) # turtle向后移动450像素
turtle.pendown()
turtle.pensize(25) # 设置画笔大小
turtle.seth(-40) # 给画笔的方向设置一个初始度数方向-40
listcolor=["purple" ,"blue" ,"cyan", "green", "yellow", "orange"] #放入颜色名称

# the body of the python
for i in range(6):
    turtle.pencolor(listcolor[i])
    turtle.circle(40 , 80)
    turtle.circle(-40, 80)

# the head of the python
turtle.pencolor("red")
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
