# 打印字符串中字母的频数（降序）
# 2020-11-05
# fyj

def count(string_demo):
    list_demo = list(string_demo)
    word = {}                          # 空字典
    for item in list_demo:             # 计数
        word[item] = word.get(item,0) + 1

    d_order = dict(sorted(word.items(),key=lambda x:x[1],reverse=True))  # 对字典按照值大小排序（逆序）

    for i in d_order.keys():                           # 打印键值对
        print(i,d_order[i])

def main():
    str = input("请输入字符串: ")
    count(str)

main()

