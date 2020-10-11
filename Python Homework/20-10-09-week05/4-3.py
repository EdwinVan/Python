# 输入两个整数，求最大公约数 4-3.py
# fyj
# 2020/10/11

while True:
    print("请输入两个整数：")
    num_1 = input(); num_2 = input()
    if num_1.isnumeric() and num_2.isnumeric():
        num_1 = eval(num_1); num_2 = eval(num_2)
        break
    else:
        print("输入有误，请输入两个整数！")

if num_1 == num_2:
    print("最大公约数和最小公倍数：{}".format(num_2))

else:
    # 被除数为较大的那个数，除数为较小的那个数
    if num_1 > num_2:
        dividend = num_1; divisor = num_2   # dividend被除数       divisor除数
    else:
        dividend = num_2; divisor = num_1

    while True:
        remainder = dividend % divisor      # remainder余数
        if remainder == 0:
            print("最大公约数:{} 最小公倍数:{}".format(divisor,int(num_1*num_2/divisor)))
            # 最小公约数为辗转相除法余数为0时除数的值，最大公倍数为原整数的积除以最大公约数
            break
        else:
            dividend = divisor
            divisor = remainder





