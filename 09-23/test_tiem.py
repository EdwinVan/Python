# 了解time.time()函数作用机理
# 2020-09-23
# fyj

import time
a = time.time()
while True:
    print(time.time()-a)
    print(time.asctime())