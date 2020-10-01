# 单行进度条-借助time库函数sleep()
# 2020/09/23
# fyj

import time

print("***进程开始***")

a = time.time()
for i in range(101):
    time.sleep(0.1)
    a = int(i / 10)
    b = 10 - a
    print("\r%s%s%d%%" %("+"*a, '-'*b, i),end="")
    print("",end="")
b = time.time()
c = b - a
print("\n***进程结束***",end="")
