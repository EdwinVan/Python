# 统计字符串字母频数
# fyj
# 2020-10-30

def countChar(s):
    outPut=[0 for i in range(26)]
    for item in s:
        if item.isalpha()!=0:
            index=ord(item.lower())-97
            outPut[index]+=1
    return outPut

string=input("输入字符串->")
print(countChar(string))