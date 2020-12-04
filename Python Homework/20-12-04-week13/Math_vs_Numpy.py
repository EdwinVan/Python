# 对比math库和numpy库的运行速度
# 2020-12-04
# fyj

import math
import numpy
import time

num = 1000

# numpy库
x = numpy.arange(1, num, 0.01)
x_1 = time.perf_counter()
for i, item in enumerate(x):
    # x[i] = numpy.power(numpy.sin(item), 2)
    # numpy.sin(item)
    x[i] = numpy.power(item, 2)
x_2 = time.perf_counter()
time_numpy = x_2 - x_1

# math库
y = numpy.arange(1, num, 0.01)
y_1 = time.perf_counter()
for i, item in enumerate(y):
    # y[i] = math.pow(math.sin(item), 2)
    # math.sin(item)
    y[i] = math.pow(item, 2)
y_2 = time.perf_counter()
time_math = y_2 - y_1

if time_math > time_numpy:
    print("Numpy库运算更快\n")
    print("Math 库用时:{}".format(time_math))
    print("Numpy库用时:{}".format(time_numpy))
elif time_math == time_numpy:
    print("两个库运算一样快\n")
    print("用时:{}".format(time_math))
else:
    print("Math库运算更快\n")
    print("Math 库用时:{}".format(time_math))
    print("Numpy库用时:{}".format(time_numpy))