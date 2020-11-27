# Stock.py 抓取 cnn财经网站 道指成分股数据并将30家公司的代码、公司名称和最近一次成交价放到一个列表中输出
# 2020-11-27
# fyj

import requests
import re
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36', 'cookie': 'FastAB=0=5349,1=1574,2=6630,3=9964,4=2385,5=1542,6=5728,7=6830,8=2732,9=7323; OptanonControl=ccc=CN&otvers=&reg=global&pctm=0&vers=3.0.1; optimizelyEndUserId=oeu1606440340953r0.5018483549931423; s_fid=382057101C837575-172276DF8CB73633; s_vi=[CS]v1|2FE02AD505159F36-60000A3139979F65[CE]; _cb_ls=1; _cb=CKCvdhCH6f7fB9rXa6; OB-USER-TOKEN=7b0f579c-1d9e-4f0c-a11b-1e34657bc081; ug=5fc055c00ea54b0a3f868800130ccaa1; ugs=1; __qca=P0-721357702-1606440396223; __gads=ID=ade737db7bc2145e:T=1606440420:S=ALNI_MZ_yqsQy26SqnS0z6mbjPnEz7cMEw; ajs_anonymous_id=%22c7cd80b1-a6b8-4003-8d75-bc39d53554eb%22; _fbp=fb.1.1606440640530.80863511; WSOD%5FxrefSymbol=INDU; last5stocks=INDU%2BAAPL%2BGOOG%2BGE%2BF%2BC; WSOD%5FshowNewsDailyMarketReport=1; WSOD%5FshowNews=1; SelectedEdition=edition; countryCode=CN; stateCode=CQ; geoData=lianhe|CQ|409105|CN|AS|800|broadband; usprivacy=1---; cnprevpage_pn=mny%3Ao%3Amoney%3A%2Fdata%2Fhotstocks%2F; s_cc=true; s_sq=%5B%5BB%5D%5D; _cb_svref=null; bounceClientVisit340v=N4IgNgDiBcIBYBcEQM4FIDMBBNAmAYnvgLYD2AdgKYCeAdAMbnkOnFEAmAhgp0XKQhQJS9ANboCIADQgATjBAgAvkA; OptanonAlertBoxClosed=2020-11-27T02:54:50.304Z; _chartbeat2=.1606440374918.1606445692512.1.C6keK0oiMxxBLFQRbBO8gMQCHhUjK.2; OptanonConsent=isIABGlobal=false&datestamp=Fri+Nov+27+2020+10%3A54%3A52+GMT%2B0800+(China+Standard+Time)&version=6.4.0&hosts=&landingPath=NotLandingPage&groups=smv%3A1%2Cpfv%3A1%2Cpzv%3A1%2Cven%3A1%2Csav%3A1%2Cadv%3A1%2CBG173%3A1%2Cpf%3A1%2Cpz%3A1%2Csa%3A1%2Cad%3A1%2Csm%3A1%2Ctdc%3A1%2Ccos%3A1%2Cdid%3A1%2Cdlk%3A1%2Cpcp%3A1%2Cdsa%3A1%2Cmra%3A1%2Cmap%3A1%2Cpap%3A1%2Cgld%3A1%2Cpad%3A1%2Cpdd%3A1%2Csid%3A1%2Ccad%3A1%2Csec%3A1%2Cmcp%3A1%2Cpcd%3A1%2Creq%3A1&AwaitingReconsent=false&geolocation=CN%3BCQ; session_depth=money.cnn.com%3D2%7C176917733%3D2; hbcm_sd=2%7C1606445615029'
} # 模拟浏览器访问

time.sleep(3)   # 延迟3秒进行爬虫操作
URL = 'https://money.cnn.com/data/hotstocks/index.html'  # 目标网址
r = requests.get(URL, headers=headers)

reg = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_aRight"><.*?>(.*?)<\/span>')    # 预编译正则表达式
ans = re.findall(reg, r.text)   # 利用正则表达式解析内容

print("{:<7}{:<36}{:<10}".format('Code', 'Name', 'Prize'))   # 公司代码、公司名称、最近一次成交价
for key in ans:
    print("{:<7}{:<36}{:<10}".format(key[0], key[1], key[2]))
