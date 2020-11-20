# 词云库wordcloud 哈姆雷人物统计并输出位图片
# fyj
# 2020-11-20

import wordcloud

# 要排除的不是人名的词
excludes = {"the","lord","sir","o","e","ay","and","no","but","exit","for"}
txt = open("哈姆雷特_En.txt").read()
txt = txt.lower()
for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
    txt = txt.replace(ch," ")
words = txt.split()
counts = {}                   # 使用字典保存人名和词频

for word in words:
    counts[word] = counts.get(word,0)+1

# 要排除的词汇
for word in excludes:
    del(counts[word])

# 转换成list，按词频排序
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
words = []
for i in range(10):
    print(items[i][0])
    words.append(items[i][0])

str = ' '.join(words)
w = wordcloud.WordCloud(max_words=10,\
                        min_font_size=20,max_font_size=40,\
                        font_path='H:/Edwin/Desktop/SimSun.ttf')

w.generate(str)
w.to_file('H:/Edwin/Desktop/Python/Python Homework/20-11-20-week11/哈姆雷特.png')