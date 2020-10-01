# 自主画一只python
# 2020/09/19
# fyj

import turtle

turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.seth(-40)

turtle.pensize(25)
turtle.pencolor("blue")


# the body of the python
for i in range(5):
    turtle.circle(40,80)
    turtle.circle(-40,80)

# the head of the python
turtle.circle(40,230)
turtle.forward(30)
