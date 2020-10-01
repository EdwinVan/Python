# 迭代器与类
# 创建一个返回数字的迭代器，初始值为 1，逐步递增 1
# 2020-09-13
# fyj


class MyNumbers:
 def __iter__(self):
    self.a = 1
    return self
 
 def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)
 
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


