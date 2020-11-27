# Crawler.py 获取豆瓣作品的评论内容
# 2020-11-26
# fyj

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}     # 模拟浏览器访问
r = requests.get('https://book.douban.com/subject/3803820/comments/',headers = headers)
soup = BeautifulSoup(r.text,'lxml')
pattern = soup.find_all('span','short')  # 返回值为列表
i = 0
for item in pattern:
    i+=1
    print(i)
    print(item.string)