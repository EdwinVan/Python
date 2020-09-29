# Daydayup365-“三天打鱼两天晒网”式学习
# 2020/09/18
# fyj

dayup,dayfactor = 1.0, 0.01 #初始设为1.0，每天变化为前一天的%1
for i in range(365):
    if i % 5 in [0, 1, 2]:
        dayup = dayup * (1 + dayfactor) # 提升
    else:
        dayup = dayup * (1 - dayfactor) # 下降
print("三天打鱼两天晒网式学习后一年：{:.2f}." .format(dayup))
