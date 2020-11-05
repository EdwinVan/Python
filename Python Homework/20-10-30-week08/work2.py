# 寻找输入数字中的全数字pandigital
# 2020-10-30
# fyj

def pandigital(str):
    i = 1
    maxnum = int(max(str))
    while(i <= maxnum):
        j = 0
        if string[j] == i:
            i += 1
            if i == maxnum:
                return str
        else:
            j += 1
            if j == len(str) - 1:
                break

num_demo = input("-> ")
num = num_demo.split(sep=',',maxsplit=-1)
for string in num:
    print("{}".format(string))
    print("全数字: {}\n".format(pandigital(string)))
