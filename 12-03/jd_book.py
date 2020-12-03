# 爬取京东网搜索词为‘python’时前50页的数据，保存到本地文件
# 2020-12-03
# fyj

import requests
from lxml import etree
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
    'path': '/s_new.php?keyword=Python&wq=Python&page=2&s=30&scrolling=y&log_id=1607004140579.5994&tpl=2_M&isList=0&show_items=12737107,12842874,11993134,12353915,12941930,12398725,34608882177,12452929,12899078,12186192,12279949,12456107,12691621,12929270,10605675311,12952982,12829246,11943853,12409581,12467272,11681561,12128326,12451724,12859710,12661197,12988848,12654873,12594658,12627795,12403048',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.5,zh;q=0.3',
    'Referer': 'https://www.jd.com/',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'TE': 'Trailers',
}  # 模拟浏览器访问
# '''

headers = {
    'authority': 'search.jd.com',
    'method': 'GET',
    'path': '/s_new.php?keyword=Python&wq=Python&page=2&s=30&scrolling=y&log_id=1607005945025.9357&tpl=2_M&isList=0&show_items=12737107,12842874,11993134,12353915,12941930,12398725,34608882177,12452929,12899078,12186192,12279949,12456107,12691621,12929270,10605675311,12952982,12829246,11943853,12409581,12467272,11681561,12128326,12451724,12859710,12661197,12988848,12654873,12594658,12627795,12403048',
    'scheme': 'https',
    'referer': 'https://search.jd.com/Search?keyword=Python&enc=utf-8&wq=Python&pvid=0dffe8096e364b1dafb80b67dc518999',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'Cookie': 'unpl=V2_ZzNtbUpTQEYlDRVUKE1eUmIDQl1KVhYQJgtCU30bWFVmAhcJclRCFnQURldnGF4UZwQZXUdcRh1FCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZH8RVARlARdcS2dzEkU4dlF5HF0CZzMTbUNnAUEpDUdWexFUSGMLGlxAVUYUfDhHZHg%3d; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_952ba4b1be3f41a190d4b256735a004e|1606983291952; __jdu=599033408; areaId=4; PCSYCityID=CN_500000_500100_0; shshshfpa=66cf22ce-a655-262c-2ea4-576d6ce9dd56-1606983294; shshshfpb=og3ngtxaAT8F74CtESii9uw%3D%3D; rkv=1.0; qrsc=3; _pst=jd_5a6f7af9ec598; unick=jd_5a6f7af9ec598; pin=jd_5a6f7af9ec598; _tp=%2BXACCtS9ikFpGFeF41iOV8Ow3q6HdaCBUpat8abD9GQ%3D; pinId=unL8Rf8N7CnJEfG-BR0XvLV9-x-f3wj7; ipLoc-djd=4-50953-50980-0; __jdc=122270672; __jda=122270672.599033408.1606983291.1606997361.1607002106.4; shshshfp=c36ca7fa3d820251905d0bfbe775c4e7; 3AB9D23F7A4B3C9B=DDPQ2T4ACCY4WW7AIAZE3HK7P5O5OTHMDW2RDDH4FR7GTNOZ6IAXJX2RJW34NVTURRZ7SCAVNHQAH6WXX7GKFDG26U; __jdb=122270672.17.599033408|4.1607002106; shshshsID=c055a8dff9edf5f2298c2c06df0ee9f4_15_1607005947899; thor=0A620587C22D3B1438837A656A1F8594C5FFD122EA02E17EE10F7EA189E0EB5BEF9DC5B62C12718A9148800FB4694ACF2BE38886D5A2A58F5BE23DBBC1D9AF5435F53B0D2715148EAFA0DFA075D95FF6236A3B8B56C9A8AFCC7B3135BCC844119CA4E2381CFC9396D43488627A6D6CB2475ABBA8F3EBAAD600D3EFD82EB48F279041F34BC5E75521F3A3089EDF95829F6283CF1A7041CEA8CF3AC4FD63BEF821',
}



URL = 'https://search.jd.com/Search?keyword=python&wq=python&page=1&s=1&click=0'     # 第一页网址
r = requests.get(URL, headers=headers, timeout=20)
Book_Info = r.text
Book_Info_html = etree.HTML(Book_Info)  # 初始化生成一个XPath解析对象

# 获取商品属性有两种xpath差异
# price = Book_Info_html.xpath('//li/div/div[@class="p-price"]/strong/i/text()')
price = Book_Info_html.xpath('//li/div/div[2]/strong/i/text()')
# price_2 = Book_Info_html2.xpath('//li/div/div/div[@class="gl-i-tab-content"]/div[@class="tab-content-item tab-cnt-i-selected"]/div[@class="p-price"]/strong/i/text()')
price_2 = Book_Info_html.xpath('//li/div/div/div[2]/div[1]/div[2]/strong/i/text()')

# 输出信息
for i, item in enumerate(price):
    print(i+1, item)

print("------------------------")

for i, item in enumerate(price_2):
    print(i+1+len(price), item)

# Book_Info_result = etree.tostring(Book_Info_html,encoding='utf-8') # 解析对象输出代码
# print(Book_Info_result.decode('utf-8'))

# copy full xpath
# 1 /html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[2]/strong/i
# 2 /html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[3]/div/div/div[2]/div[1]/div[2]/strong/i
# 3 /html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[4]/div/div/div[2]/div[1]/div[2]/strong/i

# 4 /html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[60]/div/div[2]/strong/i
