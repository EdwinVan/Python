#温度转换.py

s = input("温度和温度单位:")

if s[-1] in ["c","C"]:
    F=eval(s[0:-1])*1.8+32
    print(F)
elif s[-1] in ["f","F"]:
    C=(eval(s[0:-1])-32)/1.8
    print(C)
else:
    print("输入有误，请重试！")
