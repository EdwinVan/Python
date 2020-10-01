# daydayup 一周中学习进步5天，退步两天（每天退步前一天的%1），问要达到37.78，每天至少需要进步多少
# 20-09-22
# fyj

def Dayup(df):
    day = 1.0

    for i in range(365):
        if i % 7 in [6,0]:
            day = (1 - 0.01) * day
        else:
            day = (1 + df) * day

    return day

updayfactor = 0.01
while (Dayup(updayfactor)<37.78):
    updayfactor += 0.001

print("这种方式下，每天的努力参数至少为{:.3f}，才能达到每天都进步时那样的成果".format(updayfactor))