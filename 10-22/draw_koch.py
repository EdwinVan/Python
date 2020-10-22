# 画科赫雪花 draw_koch.py
# 2020-10-22
# fyj

import turtle

turtle.pensize(3) 
turtle.speed(0)  # 将turtle的速度调快

def draw_koch(size,n):  # 递归调用函数drae_koch()画雪花
    if n == 0:
        turtle.fd(size);  
    else:
        for ancle in [60,-120,60,0]:
            draw_koch(size/3,n-1)
            turtle.left(ancle)

def main():
    turtle.pu()    # 设置turtle起始点
    turtle.fd(-300)
    turtle.pd()   
    
    size = eval(input("请输入0阶时的直线长度: "))
    n = eval(input("请输入阶数: "))
    
    for i in range(3):       
        draw_koch(size,n)
        turtle.right(120)

    turtle.hideturtle()

main()

