import requests
import re
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}  # 模拟浏览器访问


def resultList():
    time.sleep(3)
    r = requests.get('https://money.cnn.com/data/hotstocks/index.html',headers = headers)
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
    result = re.findall(search_pattern, r.text)
    return result

def main():
    results = resultList()
    print(results)

main()


