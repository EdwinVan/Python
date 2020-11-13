# 读取文本数据，根据数据画图
# fyj
# 2020-11-13

import turtle

turtle.setup(1.0,1.0,None,None)
turtle.pensize(5)
turtle.pencolor("blue")

lst = []
with open('data.txt') as f:
    for line in f:
        line = line.replace('\n','')
        lst.append(list(map(eval,line.split(','))))

for item in lst:
    turtle.fd(item[0])
    if item[1] == 0:
        turtle.left(item[2])
    else:
        turtle.right(item[2])
    turtle.pencolor(item[3],item[4],item[5])

turtle.hideturtle()