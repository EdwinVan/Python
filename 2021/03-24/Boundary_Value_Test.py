# 进行锐角三角形的边界值判定
# Boundary_Value_Test.py
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
    elif 0 < a < 90 and 0 < b < 90 and 0 < c < 90:
        print("{:<5} {:<5} {:<5}".format(a, b, c), end=" ")
        print("锐角三角形")
    else:
        print("{:<5} {:<5} {:<5}".format(a, b, c), end=" ")
        print("非锐角三角形")


def main():
    values = [[89, 89, 2], [178, 1, 1], [87, 91, 2], [100, 40, 40], [60, 60, 60], [90, 45, 45], [88, 90, 2],
              [0, 60, 120], [180, 0, 0]]
    for value in values:
        do_test(value[0], value[1], value[2])


main()


