# .\Python Code\9-25\word_cut_plus.py
# Description: 统计txt文档中的单词及其出现的频数
# Auth: fyj
# Date: 2020-09-25
# Python 3.8.6 on Pycharm

import time
start_Time = time.time()              # 开始计时
book = open('H:\Edwin\Desktop\Little Prince.txt')
str = book.read()                     # 读取txt文档内容
book.close()                          # 关闭文件

all_Punctuation = "12345\"67890,.+-*/\\‘?!:;~^&《》\'<>[]{}_"       # 此列表保存将要去掉的字符
str2 = str.lower()                    # 将字母都置为小写
len_str2 = len(str2)
for i in range(len_str2):            # 将所有除了英文单词以外的符号换成空格
    if str2[i] in all_Punctuation:
        str2 = str2.replace(str2[i]," ")

str3 = str2.split(sep=None, maxsplit=-1)  # 以空格分隔开

the_num = []                         # 创建空列表
the_word = []                        # 创建空列表
list_words = [the_word,the_num]      # 采用嵌套list,一个保存单词，一个保存相应词频

for m in range(len(str3)):           # 开始遍历str3，
    if str3[m] not in list_words[0]: # 若第一次遇到该单词，则将此单词加入到list_word[0]，相应词频置为1
        list_words[0].append(str3[m])
        list_words[1].append(1)
    elif str3[m] in list_words[0]:                            # 若非初次遇到该单词，此单词数量+1
        for j in range(len(list_words[0])):
            if list_words[0][j] == str3[m]:
                list_words[1][j] += 1

print("文件扫描结束！")
print("原文件共{}词".format(len(str3)))
print("***详细结果3秒后呈现***")
time.sleep(3)

print("其中各自频次为:")
for n in range(len(list_words[0])):
    print("{:.<15}{:.>15}    Time:{:.2f}S".format(list_words[0][n], list_words[1][n],(time.time()-start_Time)))  # 输出单词与词频
    time.sleep(0.002)                  # 此句用于动态放出查询结果,运行约10秒

print("程序结束！")
end_Time = time.time()                 # 结束时间
the_Time = end_Time - start_Time
print("用时：{:.2f}S".format(the_Time))

for y in range(len(list_words[0])):    # 冒泡排序
    for z in range(len(list_words[0])-1):
        if list_words[1][z] > list_words[1][z+1]:
            temp_num = list_words[1][z+1]
            temp_word = list_words[0][z+1]
            list_words[1][z+1] = list_words[1][z]
            list_words[0][z+1] = list_words[0][z]
            list_words[1][z] = temp_num
            list_words[0][z] = temp_word

print("Top10：")
word_num = len(list_words[0])
print("{:.<15}{:.>15}".format("English Word","Num"))
for num in range(10):
    time.sleep(0.5)
    print("{:.<15}{:.>15}".format(list_words[0][word_num-num-1], list_words[1][word_num-num-1]))  # 输出单词与词频

