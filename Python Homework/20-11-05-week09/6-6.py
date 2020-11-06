# 统计《红楼梦》中前20位出场最多的人物
# 2020-11-06
# fyj

import jieba

excludes = {"什么","一个","我们","那里","你们","如今","说道","知道","起来","姑娘","这里","出来","他们","众人","自己","一面"}
txt = open("红楼梦.txt",encoding='gb18030').read()

words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        rword = word
    counts[rword] = counts.get(rword,0)+1

for word in excludes:
    del(counts[word])

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
