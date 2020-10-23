# 判定一个元素是否在列表中重复出现 6-2.py
# 2020-10-23
# fyj


def judge(list,elem):
    for i in range(len(list)):
        if elem == list[i]:
            return True

def main():
    list = [1,2,3,4,5,6,7,8,9]
    elem = 0
    if(judge(list,elem)==True):
        print("元素在列表中")
    else:
        print("元素不在列表中")

main()