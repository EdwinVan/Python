# 爬取京东网搜索词为‘python’时前50页的数据{商品名、价格}，保存到本地文件
# 2020-12-04
# fyj

import requests
from lxml import etree
import csv
import time

web_page_num = 2  # 获取的页数


# 第n页前30条商品数据
def goods_info_first(n):
    headers = {
        'authority': 'search.jd.com',
        'method': 'GET',
        'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=4&s=84&scrolling=y&log_id=1529828108.22071&tpl=3_M&show_items=7651927,7367120,7056868,7419252,6001239,5934182,4554969,3893501,7421462,6577495,26480543553,7345757,4483120,6176077,6932795,7336429,5963066,5283387,25722468892,7425622,4768461',
        'scheme': 'https',
        'referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=3&s=58&click=0',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'Cookie':'qrsc=3; pinId=RAGa4xMoVrs; xtest=1210.cf6b6759; ipLocation=%u5E7F%u4E1C; _jrda=5; TrackID=1aUdbc9HHS2MdEzabuYEyED1iDJaLWwBAfGBfyIHJZCLWKfWaB_KHKIMX9Vj9_2wUakxuSLAO9AFtB2U0SsAD-mXIh5rIfuDiSHSNhZcsJvg; shshshfpa=17943c91-d534-104f-a035-6e1719740bb6-1525571955; shshshfpb=2f200f7c5265e4af999b95b20d90e6618559f7251020a80ea1aee61500; cn=0; 3AB9D23F7A4B3C9B=QFOFIDQSIC7TZDQ7U4RPNYNFQN7S26SFCQQGTC3YU5UZQJZUBNPEXMX7O3R7SIRBTTJ72AXC4S3IJ46ESBLTNHD37U; ipLoc-djd=19-1607-3638-3638.608841570; __jdu=930036140; user-key=31a7628c-a9b2-44b0-8147-f10a9e597d6f; areaId=19; __jdv=122270672|direct|-|none|-|1529893590075; PCSYCityID=25; mt_xid=V2_52007VwsQU1xaVVoaSClUA2YLEAdbWk5YSk9MQAA0BBZOVQ0ADwNLGlUAZwQXVQpaAlkvShhcDHsCFU5eXENaGkIZWg5nAyJQbVhiWR9BGlUNZwoWYl1dVF0%3D; __jdc=122270672; shshshfp=72ec41b59960ea9a26956307465948f6; rkv=V0700; __jda=122270672.930036140.-.1529979524.1529984840.85; __jdb=122270672.1.930036140|85.1529984840; shshshsID=f797fbad20f4e576e9c30d1c381ecbb1_1_1529984840145'
    }

    url = 'https://search.jd.com/Search?keyword=python&wq=python&page=' + str(2*n-1) + '&s=' + str(-4+(n-1)*60) + '&click=0'  # 第n页网址
    r = requests.get(url, headers=headers, timeout=30)

    # 指定编码方式，不然会出现乱码
    r.encoding = 'utf-8'
    book_info = etree.HTML(r.text)  # 初始化生成一个XPath解析对象

    # 获取商品属性有两种xpath差异,需要分别考虑
    # 价格
    price = book_info.xpath('//li/div/div[2]/strong/i/text()')   # price为list类型
    price_2 = book_info.xpath('//li/div/div/div[2]/div[1]/div[2]/strong/i/text()')
    # 书名
    name = book_info.xpath('//li/div/div[3]/a/em/text()')
    name_2 = book_info.xpath('//li/div/div/div[2]/div[1]/div[3]/a/em/text()')

    # 此段代码用于测试
    # # 打印输出获取的数据
    # print("第{}页 加载数据".format(n))
    # for i, item in enumerate(price):
    #     print(i + 1, item, name[i])
    #
    # print("------------------------")
    #
    # for i, item in enumerate(price_2):
    #     print(i + 1 + len(price), item, name_2[i])

    with open('JD_Goods.csv', 'a', newline='', encoding='utf-8') as f:  # 不加newline=''的话csv中两条相邻数据间会空出一行
        write = csv.writer(f)
        write.writerow(['Name', 'Price'])  # 需要加[]中括号，否则字符串会分格写入csv
        for i in range(len(price)):
            write.writerow([name[i], price[i]])
        for i in range(len(price_2)):
            write.writerow([name_2[i], price_2[i]])
    f.close()


# 第n页后30条商品数据
def goods_info_end(n):
    a = time.time()
    b = '%.5f' % a
    headers = {
        'authority': 'search.jd.com',
        'method': 'GET',
        'path': '/s_new.php?keyword=python&wq=python&page=2&s=30&scrolling=y&log_id=1607044997161.3428',
        'scheme': 'https',
        'referer': 'https://search.jd.com/Search?keyword=python&wq=python&page=1&s=1&click=0',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'Cookie': 'unpl=V2_ZzNtbUpTQEYlDRVUKE1eUmIDQl1KVhYQJgtCU30bWFVmAhcJclRCFnQURldnGF4UZwQZXUdcRh1FCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZH8RVARlARdcS2dzEkU4dlF5HF0CZzMTbUNnAUEpDUdWexFUSGMLGlxAVUYUfDhHZHg%3d; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_952ba4b1be3f41a190d4b256735a004e|1606983291952; __jdu=599033408; areaId=4; PCSYCityID=CN_500000_500100_0; shshshfpa=66cf22ce-a655-262c-2ea4-576d6ce9dd56-1606983294; shshshfpb=og3ngtxaAT8F74CtESii9uw%3D%3D; qrsc=3; _pst=jd_5a6f7af9ec598; unick=jd_5a6f7af9ec598; pin=jd_5a6f7af9ec598; _tp=%2BXACCtS9ikFpGFeF41iOV8Ow3q6HdaCBUpat8abD9GQ%3D; ipLoc-djd=4-50953-50980-0; shshshfp=c36ca7fa3d820251905d0bfbe775c4e7; 3AB9D23F7A4B3C9B=DDPQ2T4ACCY4WW7AIAZE3HK7P5O5OTHMDW2RDDH4FR7GTNOZ6IAXJX2RJW34NVTURRZ7SCAVNHQAH6WXX7GKFDG26U; __jda=122270672.599033408.1606983291.1607002106.1607041959.5; __jdc=122270672; rkv=1.0; __jdb=122270672.6.599033408|5.1607041959; shshshsID=8398b9a90f8e3c9d3888ae26717b1c3a_6_1607044998121'
    }

    # 第n页的动态加载地址
    url = 'https://search.jd.com/s_new.php?keyword=python&wq=python&page=' + str(2*n) + '&s=' + str(48*n-20) + '&scrolling=y&log_id=' + str(b)
    r = requests.get(url, headers=headers, timeout=30)

    # 指定编码方式，不然会出现乱码
    r.encoding = 'utf-8'
    book_info = etree.HTML(r.text)  # 初始化生成一个XPath解析对象
    # 获取商品属性有两种xpath差异,需要分别考虑
    # 价格
    price = book_info.xpath('//li/div/div[2]/strong/i/text()')  # price为list类型
    price_2 = book_info.xpath('//li/div/div/div[2]/div[1]/div[2]/strong/i/text()')

    # 书名
    name = book_info.xpath('//li/div/div[3]/a/em/text()')
    name_2 = book_info.xpath('//li/div/div/div[2]/div[1]/div[3]/a/em/text()')

    with open('JD_Goods.csv', 'a', newline='', encoding='utf-8') as f:  # 不加newline=''的话csv中两条相邻数据间会空出一行
        write = csv.writer(f)
        for i in range(len(price)):
            write.writerow([name[i], price[i]])
        for i in range(len(price_2)):
            write.writerow([name_2[i], price_2[i]])
    f.close()


def main():
    print("*******************")
    print("程序开始")
    start = time.time()
    for n in range(1, web_page_num):
        goods_info_first(n)
        goods_info_end(n)
    end = time.time()
    print("程序结束，用时{:.2f}s".format(end-start))
    print("*******************")


main()














# Book_Info_result = etree.tostring(Book_Info_html,encoding='utf-8') # 解析对象输出代码
# print(Book_Info_result.decode('utf-8'))

# 价格 copy full xpath
# li[1]/div/div[2]/strong/i
# li[3]/div/div/div[2]/div[1]/div[2]/strong/i
# li[4]/div/div/div[2]/div[1]/div[2]/strong/i
# li[60]/div/div[2]/strong/i

# 书名
# li[1]/div/div[3]/a/em/text()[1]
# li[3]/div/div/div[2]/div[1]/div[3]/a/em/text()

# 商店
# li[22]/div/div/div[2]/div[1]/div[6]/text()  人民邮电
# li[23]/div/div[6]/text()  京东自营
# li[26]/div/div/div[2]/div[1]/div[6]/text()  明日科技京东旗舰店
# li[27]/div/div[6]/text()  高等教育