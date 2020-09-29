# CaesarCode凯撒密码-加密
# 2020-09-22
# fyj

str = input("请输入一串字符: ")
for i in str:
    if ord('a') <= ord(i) <= ord('z'):
        print(chr(ord(i) + 6),end="")
    else:
        print("",end=" ")
