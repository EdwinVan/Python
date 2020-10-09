# 画一朵玫瑰
# fyj
# 2020-10-09

import turtle
turtle.setup(1000,1000)
turtle.penup()

turtle.seth(90)
turtle.fd(300)
turtle.seth(0)
turtle.pendown()

turtle.pensize(6)

# 花蕊
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(30,90)
turtle.left(40)
turtle.circle(40,170)

turtle.circle(50,180)
turtle.circle(60,90)
turtle.left(-10)
turtle.circle(60,90)
turtle.circle(65,90)
turtle.left(-20)
turtle.circle(70,90)
turtle.circle(73,90)
turtle.left(-20)
turtle.circle(75,125)
turtle.seth(-95)
turtle.fd(50)


# 左边花瓣
turtle.pensize(4)
turtle.seth(95)
turtle.fd(20)
turtle.seth(-100)
turtle.circle(170,60)  # 左边花瓣左边部分

turtle.seth(45)
turtle.circle(90,80)   # 左边花瓣右边部分

turtle.seth(-180)
turtle.circle(-90,48)  

turtle.left(180)
turtle.circle(90,48)   

turtle.seth(-135)
turtle.circle(90,80)   


# 右边花瓣
turtle.left(180)
turtle.circle(-90,80)   
turtle.seth(0)

for i in range(9):
    turtle.fd(9)
    turtle.left(3)
for i in range(10):
    turtle.fd(6)
    turtle.left(8)
turtle.end_fill()

turtle.fillcolor("red")
turtle.begin_fill()

turtle.left(180)
turtle.circle(-139,100) # 右边花瓣右边部分

turtle.seth(45)
turtle.circle(90,80)   # 左边花瓣右边部分

turtle.seth(-180)
turtle.circle(-90,48)  

turtle.left(180)
turtle.circle(90,48)   

turtle.seth(-135)
turtle.circle(90,80) 

turtle.left(180)
turtle.circle(-90,80)   
turtle.seth(0)

for i in range(9):
    turtle.fd(9)
    turtle.left(3)
for i in range(10):
    turtle.fd(6)
    turtle.left(8)
turtle.end_fill()

turtle.left(180)
turtle.circle(-139,100)   # 右边花瓣右边部分


# 花枝
turtle.seth(-90)
for i in range(20):
    turtle.fd(10)
    turtle.left(1)
turtle.left(180)
for i in range(10):
    turtle.fd(10)
    turtle.left(-1)    

# 第1片叶子（上）
turtle.seth(20)
turtle.fillcolor("green")
turtle.begin_fill()   
for i in range(10):
    turtle.fd(10)
    turtle.right(1)

turtle.penup()
turtle.left(180)
for i in range(7):
    turtle.fd(10)
    turtle.left(1)
turtle.pendown()
turtle.seth(50)

turtle.circle(-90,90)
turtle.left(-90)
turtle.circle(-90,90)
turtle.end_fill()


turtle.left(60)
turtle.fd(30)
turtle.seth(-80)
for i in range(5):
    turtle.fd(10)
    turtle.left(1)

# 第2片叶子（下）
turtle.seth(175)
turtle.fillcolor("green")
turtle.begin_fill()
for i in range(12):
    turtle.fd(10)
    turtle.right(1)

turtle.penup()
turtle.left(180)
for i in range(7):
    turtle.fd(10)
    turtle.left(1)
turtle.pendown()
turtle.seth(130)

turtle.circle(90,90)
turtle.left(90)
turtle.circle(90,90)
turtle.end_fill()

turtle.left(-47)
turtle.fd(50)
turtle.seth(-75)
for i in range(5):
    turtle.fd(10)
    turtle.left(1)






