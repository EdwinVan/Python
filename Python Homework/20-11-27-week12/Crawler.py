# Crawler2.py 抓取豆瓣作品的评论，输出评论内容并计算平均分（网页每页展示20个评论）
# 2020-11-27
# fyj

import requests
from bs4 import BeautifulSoup
import re
import time
num = 50         # 选取前50个评分数量(用于计算平均分)
global str_num   # 评论序号(如第1条......第num条)
NUM = 0          # 全局变量（一般大写）

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}  # 模拟浏览器访问

def URL_Data(url):
    p_demo = []
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    pattern = soup.find_all('span', 'short')  # 返回值为列表
    global NUM
    for item in pattern:
        NUM += 1
        print("第{}条:\n{}".format(NUM,item.string))
        if NUM == num:
            break
    pattern_s = re.compile('span class="user-stars allstar(.*) rating" ')  # 编译正则表达式，生成一个正则表达式（ Pattern ）对象
    p_demo = re.findall(pattern_s, r.text)  # 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
    return p_demo

def main():
    # 3个网页
    URL = 'https://book.douban.com/subject/1007305/comments/?limit=20&status=P&sort=new_score'  # 第一页评论的网址
    p = URL_Data(URL)
    time.sleep(3)       # 延迟3秒进行爬虫操作，防止服务器屏蔽IP
    URL = 'https://book.douban.com/subject/1007305/comments/?start=40&limit=20&status=P&sort=new_score'   # 第二页评论的网址
    p1 = URL_Data(URL)
    time.sleep(3)       # 延迟3秒进行爬虫操作，防止服务器屏蔽IP
    URL = 'https://book.douban.com/subject/1007305/comments/?start=60&limit=20&status=P&sort=new_score'   # 第三页评论的网址
    p2 = URL_Data(URL)

    for item in p1:     # 将第二页资源信息添加到列表
        p.append(item)
    for item in p2:     # 将第三页资料信息添加到列表
        p.append(item)

    # 计算评分
    s = 0               # 前num个用户的总评分初始化为0
    for i in range(num):
        s += int(p[i])  # 计算总评分
    print("\n书名：《红楼梦》:")
    print("短评前{}个用户打出总评分:{}".format(num, s))
    print("平均分:{}".format(s / num))

main()

