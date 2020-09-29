# 3.7 仿照实例4写文本进度条
# fyj

import time
scale = 10

for i in range(scale+1):
    c = (i/scale)*100
    a = '*' * (scale - i)
    b = '.' * i
    print("\rStarting [{}{}]{:.0f}%".format(b,a,c),end="")
    time.sleep(0.3)
    if i == scale:
        print("\rStarting {} Done!".format(b))