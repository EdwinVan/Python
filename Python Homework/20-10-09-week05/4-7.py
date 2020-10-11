# 改造实例一
# fyj
# 2020/10/11

while True:
    tempstr = input("请输入带有符号的温度值：")
    try:
        if tempstr[-1] in ['F', 'f']:
            c = (eval(tempstr[0:-1]) - 32) / 1.8
            print("转换后的温度是：{:.2f}C".format(c))
            break
        elif tempstr[-1] in ['c', 'F']:
            f = (eval(tempstr[0:-1]) * 1.8) + 32
            print("转换后的温度是：{:.2f}F".format(f))
            break
    except NameError:
        print("请输入正确的格式")