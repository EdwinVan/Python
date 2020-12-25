# 范玉杰  3.py
# 2018051604006
# 2020-12-25

def change(str1):
    for item in str1:
        if item.isalpha():
            if item.islower():
                str1 = str1.replace(item, item.upper())
            else:
                str1 = str1.replace(item, item.lower())

    print(str1)


def main():
    str1 = input("请输入字符: ")
    change(str1)


main()


