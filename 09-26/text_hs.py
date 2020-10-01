# 函数修改可变类型数据

def changeme(mylist):
    # 修改传入的列表
    mylist.append(['a','b','c'])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
print("函数调用前: ", mylist)
changeme(mylist)
print("函数外取值: ", mylist)