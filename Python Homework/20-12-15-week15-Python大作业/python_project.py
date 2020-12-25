# python-work.py 爬取 "人民网" 官网习大大（2012年-至今）的系列讲话原稿，制作词云
# fyj
# 2020-12-16

import requests         # 爬虫
from lxml import etree  # 解析爬虫获取的HTML
import time             # 计算时间
import wordcloud        # 词云
import jieba            # 分词
import numpy as np      # 科学计算
from PIL import Image   # 处理图片

web_num = 24      # 网页数据共24个页面
num_url = 0       # 文章url数量
num_webpage = 0   # 文章数量


# 获取全部文章的url
def get_url(page):
    headers = {
        'Accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'authority': 'search.jd.com',
        'method': 'GET',
        'content-type': 'text/javascript;charset=UTF-8',
        'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=4&s=84&scrolling=y&log_id=1529828108.22071&tpl=3_M&show_items=7651927,7367120,7056868,7419252,6001239,5934182,4554969,3893501,7421462,6577495,26480543553,7345757,4483120,6176077,6932795,7336429,5963066,5283387,25722468892,7425622,4768461',
        'scheme': 'https',
        'referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=3&s=58&click=0',
        'x-requested-with': 'XMLHttpRequest',
        'Cookie': 'qrsc=3; pinId=RAGa4xMoVrs; xtest=1210.cf6b6759; ipLocation=%u5E7F%u4E1C; _jrda=5; TrackID=1aUdbc9HHS2MdEzabuYEyED1iDJaLWwBAfGBfyIHJZCLWKfWaB_KHKIMX9Vj9_2wUakxuSLAO9AFtB2U0SsAD-mXIh5rIfuDiSHSNhZcsJvg; shshshfpa=17943c91-d534-104f-a035-6e1719740bb6-1525571955; shshshfpb=2f200f7c5265e4af999b95b20d90e6618559f7251020a80ea1aee61500; cn=0; 3AB9D23F7A4B3C9B=QFOFIDQSIC7TZDQ7U4RPNYNFQN7S26SFCQQGTC3YU5UZQJZUBNPEXMX7O3R7SIRBTTJ72AXC4S3IJ46ESBLTNHD37U; ipLoc-djd=19-1607-3638-3638.608841570; __jdu=930036140; user-key=31a7628c-a9b2-44b0-8147-f10a9e597d6f; areaId=19; __jdv=122270672|direct|-|none|-|1529893590075; PCSYCityID=25; mt_xid=V2_52007VwsQU1xaVVoaSClUA2YLEAdbWk5YSk9MQAA0BBZOVQ0ADwNLGlUAZwQXVQpaAlkvShhcDHsCFU5eXENaGkIZWg5nAyJQbVhiWR9BGlUNZwoWYl1dVF0%3D; __jdc=122270672; shshshfp=72ec41b59960ea9a26956307465948f6; rkv=V0700; __jda=122270672.930036140.-.1529979524.1529984840.85; __jdb=122270672.1.930036140|85.1529984840; shshshsID=f797fbad20f4e576e9c30d1c381ecbb1_1_1529984840145'
    }  # 模拟浏览器访问

    url = 'http://jhsjk.people.cn/result/' + str(page) + '?form=706&else=501'  # 第page页的网址
    r = requests.get(url, headers=headers, timeout=30)

    r.encoding = 'utf-8'  # 指定编码方式，防止出现乱码
    speak_link = etree.HTML(r.text)  # 初始化生成一个XPath解析对象,保存原文的链接地址

    link = speak_link.xpath('//body/div[5]/div[2]/ul/li/a/@href')

    # 此段代码用于测试
    # 打印输出获取的数据
    # for i, item in enumerate(link):
    #     print(i+1, item)

    # 将第page页获取的文章链接保存到本地文件 speak_url.txt
    with open('speak_url.txt', 'a', encoding='utf-8') as f:
        for item in link:
            f.write('{}\n'.format(item))   # 按行写入url数据
            global num_url   # url数量+1
            num_url += 1


# 根据文章url访问文章
def get_details():

    headers = {
        'Accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'authority': 'search.jd.com',
        'method': 'GET',
        'content-type': 'text/javascript;charset=UTF-8',
        'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=4&s=84&scrolling=y&log_id=1529828108.22071&tpl=3_M&show_items=7651927,7367120,7056868,7419252,6001239,5934182,4554969,3893501,7421462,6577495,26480543553,7345757,4483120,6176077,6932795,7336429,5963066,5283387,25722468892,7425622,4768461',
        'scheme': 'https',
        'referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=3&s=58&click=0',
        'x-requested-with': 'XMLHttpRequest',
        'Cookie': 'qrsc=3; pinId=RAGa4xMoVrs; xtest=1210.cf6b6759; ipLocation=%u5E7F%u4E1C; _jrda=5; TrackID=1aUdbc9HHS2MdEzabuYEyED1iDJaLWwBAfGBfyIHJZCLWKfWaB_KHKIMX9Vj9_2wUakxuSLAO9AFtB2U0SsAD-mXIh5rIfuDiSHSNhZcsJvg; shshshfpa=17943c91-d534-104f-a035-6e1719740bb6-1525571955; shshshfpb=2f200f7c5265e4af999b95b20d90e6618559f7251020a80ea1aee61500; cn=0; 3AB9D23F7A4B3C9B=QFOFIDQSIC7TZDQ7U4RPNYNFQN7S26SFCQQGTC3YU5UZQJZUBNPEXMX7O3R7SIRBTTJ72AXC4S3IJ46ESBLTNHD37U; ipLoc-djd=19-1607-3638-3638.608841570; __jdu=930036140; user-key=31a7628c-a9b2-44b0-8147-f10a9e597d6f; areaId=19; __jdv=122270672|direct|-|none|-|1529893590075; PCSYCityID=25; mt_xid=V2_52007VwsQU1xaVVoaSClUA2YLEAdbWk5YSk9MQAA0BBZOVQ0ADwNLGlUAZwQXVQpaAlkvShhcDHsCFU5eXENaGkIZWg5nAyJQbVhiWR9BGlUNZwoWYl1dVF0%3D; __jdc=122270672; shshshfp=72ec41b59960ea9a26956307465948f6; rkv=V0700; __jda=122270672.930036140.-.1529979524.1529984840.85; __jdb=122270672.1.930036140|85.1529984840; shshshsID=f797fbad20f4e576e9c30d1c381ecbb1_1_1529984840145'
    }  # 模拟浏览器访问

    # 读取保存的文章链接，用列表单个保存
    url_list = []  # 初始化生成一个list变量
    with open('speak_url.txt', 'r', encoding='utf-8') as f:
        urls = f.readlines()
        list1 = []
        for i in urls:
            url_list.append(i.strip().split('\t'))  # 将文章链接增添到list列表中
            global num_webpage
            num_webpage += 1

    for i in range(len(url_list)):
        url_detail = "http://jhsjk.people.cn/" + url_list[i][0]   # 某页第i个文章地址
        r = requests.get(url_detail, headers=headers, timeout=30)
        r.encoding = 'utf-8'

        speak_detail_demo = etree.HTML(r.text)
        # /html/body/div[5]/div[2]
        details = speak_detail_demo.xpath('//body/div[5]/div[2]/p')
        with open('speak_all.txt', 'a', encoding='utf-8') as f:
            for item in details:
                f.write(item.xpath('string(.)'))   # 拿取嵌套结点的text内容


# 根据获取的文章数据绘制词云
def data_wordcloud():
    # 读取词源文件
    with open("speak_all.txt", "r", encoding="utf-8") as f:
        txt = f.read()  # 直接读取f的整个文件，保存为str格式

    words = jieba.lcut(txt)      # 进行分词操作
    word_txt = " ".join(words)   # 把分词用空格连接起来
    photo = np.array(Image.open('map (2).jpg'))   # 打开(背景)图像并转化为数组对象

    # 设置词云参数
    w = wordcloud.WordCloud(
        font_path="SIMYOU.TTF",     # 字体：SIMYOU幼圆
        max_words=1000,             # 允许的最大词汇量
        max_font_size=130,          # 设置最大的字体的大小
        mask=photo,                 # 设置使用的背景图片
        background_color="white",   # 设置输出的图片的背景色
    )

    # 生成词云
    w.generate(word_txt)
    w.to_file("生成图片.png")


# 主函数
def main():
    start = time.time()
    print("***获取全部文章url开始***")
    for i in range(1, web_num+1):   # 爬取1-web_num页面的所有文章保存到本地文件 speak_all_1.txt
        print("爬取第{}页的文章url".format(i))
        get_url(i)

    global num_url
    print("***爬取全部文章url结束***")
    print("爬取文章url数量{}条到本地".format(num_url))

    print("\n开始根据url爬取文章原文并保存到本地")
    get_details()
    print("爬取文章原文数量{}条到本地".format(num_webpage))
    print("爬取文章原文结束")

    end = time.time()
    the_time = end - start
    print("程序运行结束，共用时{:.2f}S".format(the_time))

    # 绘制词云
    print("绘制词云")
    data_wordcloud()
    print("成功导出生成的图片")


main()
