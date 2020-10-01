# Name: word_cut.py
# Description: 从字符串中切割英文单词
# Auth: fyj
# Date: 2020-09-25

def word_Cut(Punctuation,in_Str_Copy):
    Str2 = in_Str_Copy.split(sep=Punctuation, maxsplit=-1)  # 以pubctuation分隔开
    in_Str_Copy = "" #中间变量
    Str_demo = "" #中间变量
    for i in range(len(Str2)):
        Str_demo = " " + Str2[i]  # 将文件列表项拼接成字符型，增加一个空格
        in_Str_Copy += Str_demo
        if i==0:
            in_Str_Copy = in_Str_Copy[1:]

    return in_Str_Copy

Str = "abc,defg hi!jk.lmn?o;pq,rs\"t uv\"wx.yz" #英文字符串
print("原文件:{}".format(Str))
print("扫描开始！")
Str_Copy = Str
all_Punctuation = [',', '.', '?', '!', '\'', '\"', ':', ';', '[', ']', '{', '}'] #此列表保存标点符号
for j in range(len(all_Punctuation)):
    Str_Copy = word_Cut(all_Punctuation[j],Str_Copy)

all_Str = Str_Copy.split(sep=" ", maxsplit=-1)  # 以空格分隔开

for j in range(len(all_Str)):
    print(all_Str[j])
all_Str2 = []
for k in range(len(all_Str)):
    if all_Str[k] not in all_Str2:
        all_Str2.append(all_Str[k])


print("扫描结束！")
print("原文件共{}词".format(len(all_Str)),end="")
print(":{}".format(all_Str2))
