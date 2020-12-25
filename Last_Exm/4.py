# 范玉杰  4.py
# 2018051604006
# 2020-12-25
import sys
inf = {}


def newusers():
    global inf
    name = input("请输入名字: ")
    if name in inf.keys():
        newusers()

    passport = input("请输入密码: ")
    inf[name] = passport
    print("注册成功!")


def oldusers():
    global inf
    name_demo = input("请输入账号: ")
    pass_demo = input("请输入密码: ")
    if name_demo in inf.keys() and pass_demo == inf[name_demo]:
        print('{}, welcome back'.format(name_demo))
    else:
        print("login incorrect")


def login():
    while True:
        print("(N)ew User Login")
        print("(O)ld User Login")
        print("(E)xit")
        i = input("请输入选项: ")
        if i == 'N':
            newusers()
        elif i == 'O':
            oldusers()
        elif i == 'N':
            sys.exit()  # 退出程序
        else:
            print("输入有误,请重新输入!")


def main():
    login()


main()