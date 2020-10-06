# 尝试新的进度条刷新方式，呈现先慢后快的效果
# fyj
# 2020-10-06

import time
length_bar = 30

for i in range(length_bar+1):
    if i < 30:
        percent = i / length_bar * 100
        str1 = '⬛' * i
        str2 = '⬜' * (length_bar - i)
        print("\r{:<3.0f}%[{}{}]".format(percent, str1, str2),end="")
        time.sleep(0.2)
    else:
        percent = i / length_bar * 100
        str1 = '⬛' * i
        str2 = '⬜' * (length_bar - i)
        print("\r{:<3.0f}%[{}{}]".format(percent, str1, str2), end="")
        time.sleep(0.08)