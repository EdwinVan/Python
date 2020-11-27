# Crawler2.py 抓取豆瓣作品的评分
# 2020-11-26
# fyj

import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}       # 模拟浏览器访问
r = requests.get('https://book.douban.com/subject/1007305/comments/?limit=20&status=P&sort=new_score',headers = headers)
soup = BeautifulSoup(r.text,'lxml')
pattern = soup.find_all('span','short')   # 返回值为列表
for item in pattern:
    print(item.string)
pattern_s = re.compile('span class="user-stars allstar(.*) rating" ')  # 编译正则表达式，生成一个正则表达式（ Pattern ）对象
p = re.findall(pattern_s,r.text)  # 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表

# 计算评分
s = 0   # 评分初始化为0
for star in p:
    s += int(star)
print("短评前{}个用户打出总评分:{}".format(len(p),s))
print("平均分:{}".format(s/len(p)))