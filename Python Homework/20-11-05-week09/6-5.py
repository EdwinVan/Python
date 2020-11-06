# 生日悖论的分析证明
# 2020-11-05
# fyj
import random



times = 1000000      # 实验样本总次数
same_bir = 0       # 每种样本下存在至少两人生日相同的频数

while times > 0:
    i = 27         # 随机生成27个生日
    bir_all = []
    while i > 0:
        m = random.randint(1,12)
        if m in [1,3,5,7,8,10,12]:
            d = random.randint(1, 31)
        elif m in [4,6,9,11]:
            d = random.randint(1, 30)
        else:
            d = random.randint(1,29)   # 2月份最大为29

        if len(str(m)) == 1 and len(str(d)) == 1 :  bir = '0' + str(m) + '0' + str(d)
        elif len(str(m)) == 1 and len(str(d)) != 1 :  bir = '0' + str(m) + str(d)
        elif len(str(m)) != 1 and len(str(d)) == 1 :  bir = str(m) + '0' + str(d)
        else: bir = str(m) + str(d)
        bir_all.append(bir)
        i -= 1
    print(bir_all)
    len_bir = len(bir_all)
    set_bir = set(bir_all)
    len_set_bir = len(set_bir)
    if(len_bir != len_set_bir):
        same_bir += 1
    times -= 1

times = 1000000
print("{}个样本中，{}个存在至少两人生日相同，概率为{:.2f}%".format(times,same_bir,same_bir/times*100))
