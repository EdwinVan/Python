# 用户输入1-7内数字，输出相应的中文星期数
# 2020-09-22
# fyj

a = "星期一星期二星期三星期四星期五星期六星期天"

while True:
    b = eval(input("请输入数字（1-7）： "))
    print(a[3*(b-1) : (3*b)])