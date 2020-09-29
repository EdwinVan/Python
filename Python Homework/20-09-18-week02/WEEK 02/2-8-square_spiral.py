# Square spiral 画正方形螺旋线
# 2020/09/18
# fyj

from turtle import *
import turtle

turtle.setup(1.0, 1.0, None, None)
a = 10  # 最内圈第一条边的长度
b = 33  # 循环圈数的一半
turtle.pendown()

for i in range(b):
    right(-90)
    turtle.fd(a)
    right(-90)
    turtle.fd(a)
    a += 10
    i += 1


right(-90)
turtle.fd(a)
right(-90)
