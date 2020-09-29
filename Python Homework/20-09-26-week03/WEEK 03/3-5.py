# 3.4 输出田字格
# fyj

a = "+ - - - - + - - - - +"
b = "|         |         |"


for i in range(11):
    if i in [0,5,10]:
        print(a)
    else:
        print(b)
