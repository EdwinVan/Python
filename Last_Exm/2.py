# 范玉杰  2.py
# 2018051604006
# 2020-12-25

n = eval(input("请输入数列项数: "))

if n <= 0:
    print("请输入大于0的整数: ")
else:
    a, b = 0, 1
    num = 1
    while True:
        print(b)
        if num == n:
            break
        a, b = b, a + b
        num += 1






