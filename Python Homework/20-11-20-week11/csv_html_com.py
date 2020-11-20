# 读取csv文件，输出格式化的html文件
# 2020-11-20
# fyj

seg1 = '''
<!DOCTYPE HTML>\n<html>\n<body>\n<meta charset=gb2312>
<h2 align=left>表4-21 笔记本电脑数据</h2>
<table border='1' align='left' width=70%>
<tr bgcolor='0D8FBF'>\n
'''
seg2 = '</tr>\n'
seg3 = '</table>\n</body>\n</html>'

# 表格的每一行数据格式
def fill_data(locls):
    seg = '<tr><td align="center">{}</td><td align="center">{}</td><td align="center">{}</td><td align="center">{}</td><td align="center">{}</td></tr>\n'.format(*locls)
    return seg

fr = open("DataFrame.csv","r",encoding='UTF-8')   # 以只读方式打开csv文件
ls = []
for line in fr:
    line = line.replace("\n","")   # 去掉csv文件中每行数据末尾的换行符'\n'
    ls.append(line.split(","))     # 以','分隔csv每行的字符串数据，保存位list
fr.close()                         # 关闭csv文件

fw = open("DataFrame.html", "w")   # 以覆盖写方式打开html文件（没有则新建）
fw.write(seg1)                     # 将seg1内容写入html

# 表格每一列宽度占比
fw.write('<th width="10%">{}</th>\n<th width="20%">{}</th>\n<th width="20%">{}</th>\n<th width="20%">{}</th>\n<th width="20%">{}</th>\n'.format(*ls[0]))
fw.write(seg2)

for i in range(len(ls)-1):         # 表格中除首行外的其他行
    fw.write(fill_data(ls[i+1]))

fw.write(seg3)
fw.close()