# 进行直角三角形的边界值判定
# Boundary_Value_Test2.py
# fyj
# 2021-03-24


def do_test(a, b, c):
    if a+b+c != 180:
        print("{:<5} {:<5} {:<5}".format(a, b, c), end=" ")
        print("非三角形")
    elif a <= 0 or b <= 0 or c <= 0:
        print("{:<5} {:<5} {:<5}".format(a, b, c), end=" ")
        print("非三角形")
    elif a >= 180 or b >= 180 or c >= 180:
        print("{:<5} {:<5} {:<5}".format(a, b, c), end=" ")
        print("非三角形")
    elif a == 90 and a + b +c == 180:
        print("{:<5} {:<5} {:<5}".format(a, b, c), end=" ")
        print("直角三角形")
    elif b == 90 and a + b + c == 180:
        print("{:<5} {:<5} {:<5}".format(a, b, c), end=" ")
        print("直角三角形")
    elif c == 90 and a + b + c == 180:
        print("{:<5} {:<5} {:<5}".format(a, b, c), end=" ")
        print("直角三角形")
    else:
        print("{:<5} {:<5} {:<5}".format(a, b, c), end=" ")
        print("非直角三角形")


def main():
    values = [[90, 45, 45], [0, 90, 90], [180, 0, 0], [89, 89, 2], [2, 92, 86], [176, 2, 2], [60, 60, 60], [120, 40, 20]]
    for value in values:
        do_test(value[0], value[1], value[2])


main()


