# 温度转换.py
# 2020/09/18
# fyj

s = eval( input("温度值： ") )
tempstr = input("温度符号： ")


if tempstr in ["c","C"]:
    F = s*1.8+32
    print("转换后的温度格式为 %dF" %(F))
elif tempstr in ["f","F"]:
    C=(s-32)/1.8
    print("转换后的温度格式为 %dC" %(C))
else:
    print("输入有误，请重试！")
