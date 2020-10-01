# 带刷新的文本进度条
# 2020/09/25
# fyj

import time
a = 20  #加载条100%时'*'的数量
print("执行开始".center(a//2,'-'))
start_time = time.time()

for i in range(a+1):
    m = '*' * i
    n = '.' * (a-i)
    cen_time = time.time()
    the_time = cen_time - start_time
    print("\r{:^3.0f}% [{}->{}] {:^3.2f}s".format(i/a*100,m,n,the_time),end="")
    time.sleep(0.2)

print("\n"+"执行结束".center(a//2,'-'))