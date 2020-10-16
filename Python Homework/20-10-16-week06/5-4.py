# 5-4.py
# 2020/10/16
# fyj
result = 1

def multi(inputnum):
    global result
    for i in range(len(inputnum)):
        result = result * inputnum[i]
    return result

def main():
    inputnum = []  # 定义一个元素类型的值
    while (True):
        num = input("请输入数字(以$作为输入结束标志): ")
        if (num == '$'):
            break
        else:
            inputnum.append(eval(num))

    print("乘积为: {}".format(multi(inputnum)))

main()
