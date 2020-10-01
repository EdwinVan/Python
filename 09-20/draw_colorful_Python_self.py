# 画一只七彩的PYTHON
# fyj
# 2020/09/20

import turtle
turtle.setup(0.5,0.5,None,None)
turtle.pensize(25)
turtle.penup()
turtle.fd(-350)
turtle.pendown()
turtle.seth(-40)
# the body of the python
list = ['purple','blue','cyan','green','yellow','orange','red']
for i in range(7):
    turtle.pencolor(list[i])
    turtle.circle(40, 80)
    turtle.circle(-40, 80)

# the head of the python
turtle.seth(0)
turtle.fd(50)
turtle.circle(40,40)

