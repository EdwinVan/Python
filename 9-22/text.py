# 单行动态刷新进度条
# 2020-9-22
# fyj

'''
i = 0
a = ""
b = ""
e = ""
while (i <= 1000000):
    i += 1
    # c = i // 1000000
    # d = 10 - c
    if i in range(100000):
        print("\r---------- 10%",end="")
    elif i in range(200000):
        print("\r+--------- 20%",end="")
    elif i in range(300000):
        print("\r++-------- %30",end="")
    elif i in range(400000):
        print("\r+++------- %40",end="")
    elif i in range(500000):
        print("\r++++------ %50",end="")
    elif i in range(600000):
        print("\r+++++----- %60",end="")
'''

''' elif i in [1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000]:
        a = "+" * c
        b = "-" * d
        e = a + b
        print("\r")
        f = i / 100000
        print("{} %{:.0f}".format(e, f), end="") 
'''


import time
f = ""
m = time.time()
b = int(m)
while (int(time.time())-b <= 60):
    c = int(time.time())
    d = int ((c - b) * 5 / 3)
    if int(int(time.time()-b)* 5 / 3) < 10:
        f = "----------"
    if int(int(time.time()-b)* 5 / 3) == 10:
        f = "+---------"
    if int(int(time.time()-b)* 5 / 3) == 20:
        f = "++--------"
    if int(int(time.time()-b)* 5 / 3) == 30:
        f = "+++-------"
    if int(int(time.time()-b)* 5 / 3) == 40:
        f = "++++------"
    if int(int(time.time()-b)* 5 / 3) == 50:
        f = "+++++-----"
    if int(int(time.time()-b)* 5 / 3) == 60:
        f = "++++++----"
    if int(int(time.time()-b)* 5 / 3) == 70:
        f = "+++++++---"
    if int(int(time.time()-b)* 5 / 3) == 80:
        f = "++++++++--"
    if int(int(time.time()-b)* 5 / 3) == 90:
        f = "+++++++++-"
    if int(int(time.time()-b)* 5 / 3) == 100:
        f = "++++++++++"
        print("\n加载完毕\n")
    print("\r{} {}%".format(f,d),end="")
