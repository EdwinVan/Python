# 英文文章词频统计
# 2020/09/25
# fyj

a = "hello,red.blue!green oppo huawei"  # 原始数据
b = a.split(sep=" ",maxsplit=-1)  #以空格分隔开
c = []
for i in range(len(b)):
    c.append(b[i])

for j in range(len(c)):
    if ',' in c[j]:
        d = c[j].split(sep=",", maxsplit=-1)  # 以','分隔开

        for m in range(len(d)):
            if '.' in d[m]:
                e = d[m].split(sep=".", maxsplit=-1)  # 以'.'分隔开

                for j in range(len(e)):
                    if '!' in e[j]:
                        g = e[j].split(sep="!", maxsplit=-1)  # 以'!'分隔开

                        for o in range(len(g)):
                            print(g[o])
                    else:
                        print(e[j])
            else:
                print(d[m])
    else:
        print(c[j])
