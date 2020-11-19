# 词云输出红楼梦的人名(Top 20)
# fyj
# 2020-11-19

import jieba
import wordcloud

# 要排除的不是人名的词
excludes = {"什么","一个","我们","那里","你们","如今","说道","知道","起来","姑娘","这里","出来","他们","众人","自己","一面","两个",
            "只见","怎么","没有","不是","不知","这个","听见","这样","进来","咱们","告诉","就是","东西","回来","只是","大家","只得",
            "丫头","这些","不敢","出去","所以","不过","的话","不好","姐姐","一时","不能","过来","心里","如此","今日","银子","几个",
            "答应","二人","还有","只管","这么","说话","一回","那边","这话","二爷","外头","打发","自然","今儿","罢了","屋里","那些",
            "听说","小丫头","奶奶","如何","问道","看见","妹妹","人家","不用","媳妇","原来","一声"}

txt = open("红楼梦.txt",encoding='gb18030').read()

# 向分词库增加分词
jieba.add_word("宝二爷")
jieba.add_word("黛玉")
jieba.add_word("宝姑娘")
jieba.add_word("香菱")
jieba.add_word("王熙凤")

words = jieba.lcut(txt)

counts = {}                   # 使用字典保存人名和词频

for word in words:
    if len(word) == 1:
        continue
    elif word == "老太太":
        rword = "贾母"
    elif word == '太太':
        rword = '王夫人'
    elif word == '凤姐' or word == '凤姐儿':
        rword = "王熙凤"
    elif word == "颦儿" or word == "林黛玉":
        rword = "黛玉"
    elif word == "老爷":
        rword = "贾政"
    elif word == "宝二爷":
        rword = "宝玉"
    elif word == "宝姑娘":
        rword = "宝钗"
    else:
        rword = word

    counts[rword] = counts.get(rword,0)+1

# 要排除的词汇
for word in excludes:
    del(counts[word])

# 转换成list，按词频排序
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
words = []
for i in range(20):
    words.append(items[i][0])

str = ' '.join(words)
w = wordcloud.WordCloud(max_words=20,\
                        min_font_size=20,max_font_size=40,\
                        font_path='H:/Edwin/Desktop/SimSun.ttf')

w.generate(str)
w.to_file('H:/Edwin/Desktop/Python/11-19/红楼梦.png')