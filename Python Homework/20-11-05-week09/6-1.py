# 6-1.py 随机生成一个密码，保存于list列表，成分限于26个字母大小写以及9个数字
# 2020-11-5
# fyj

import random

random.seed()
letter = []

# letter列表保存26个英文字母的大小写和数字0-9
for i in range(26):
    letter.append(chr(ord('A') + i))
for i in range(26):
    letter.append(chr(ord('a') + i))
for i in range(10):
    letter.append(str(i))

passport = []
for j in range(10):
    for i in range(8):
        passport_demo = []  # 放入passport的8个密码之一
        passport.append(passport_demo)
        passport[j].append(letter[random.randint(0, 61)])

passport_last = []  # 存放最终的密码结果
passport_last_demo = []  # 过度中间值
for j in range(10):
    String_demo = ""
    for i in range(8):
        String_demo += passport[j][i]

    passport_last.append(String_demo)
    print("密码{:>2.0f}-----------{}".format(j + 1, passport_last[j]))












