# 使用datetime库，以不少于十种的格式输出我的生日 5-6.py
# 2020-10-22
# fyj

import datetime

birthday = datetime.datetime(2000,1,21,2,26,36)

print(birthday.strftime("%Y-%m-%d %H:%M:%S:%p"))
print(birthday.strftime("%Y-%d-%m %H:%M:%S:%p"))
print(birthday.strftime("%m-%d-%Y %H:%M:%S:%p"))
print(birthday.strftime("%m-%Y-%d %H:%M:%S:%p"))
print(birthday.strftime("%d-%m-%Y %H:%M:%S:%p"))
print(birthday.strftime("%d-%Y-%m %H:%M:%S:%p"))

print(birthday.strftime("%p-%H:%M:%S %Y-%m-%d"))
print(birthday.strftime("%p-%H:%M:%S %m-%d-%Y"))
print(birthday.strftime("%p-%H:%M:%S %d-%m-%Y"))
print("{} 周{}".format(birthday.isoformat(),birthday.isoweekday()))