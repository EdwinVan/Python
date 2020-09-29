# 汇率兑换.py
# 2020/09/18
# fyj

print("'y'&'Y'为‘人民币’")
print("'d'&'D'为‘美元’\n")

s = input("金钱值和金钱符号：")

while s[-1] not in ['N','n']:
    if s[-1] in ["d","D"]:
        Yuan=eval(s[0:-1])*6
        print("转换后的金钱{:.2f}Yuan".format(Yuan))
    elif s[-1] in ["y","Y"]:
        Dollar= eval(s[0:-1]) / 6
        print("转换后的金钱{:.2f}Dollar".format(Dollar))
    else:
        print("输入有误，请重试！")
    
        
    s = input("\n金钱值和金钱符号：")
