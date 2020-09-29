# CaesarCode凯撒密码-解密
# 2020-09-22
# fyj

str = input("请输入待解密的明文： ")
for i in str:
    if ord('a') <= ord(i) <= ord('z'):
        print(chr(ord(i) - 6),end='')
    else:
        print(" ",end="")
