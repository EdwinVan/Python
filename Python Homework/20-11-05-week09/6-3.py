# 判定一个列表中书否有元素重复出现（利用集合） 6-2.py
# 2020-11-05
# fyj

def judge(list_elem):
    s = set(list_elem)
    if len(set)<len(list_elem):          # 传入列表中数据数和元素去重后的集合对比，若两者中后者数量较少，则说明存在相同的元素，否则不存在
        return True

def main():
    l = []
    elem = input("请输入元素（以#作为输入结束标志）: ")
    l.append(elem)
    while (elem!='#'):
        elem = input("请输入元素（以#作为输入结束标志）: ")
        l.append(elem)
    l.pop()                                            # 删除最后的输入结束符号'#'

    if(judge(l) == True):
        print("列表中存在元素出现不止一次")
    else:
        print("列表中元素都仅出现一次")

main()