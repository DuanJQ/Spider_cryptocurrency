#coding=utf-8
# -*- coding:UTF-8 -*-
import importlib
import sys
import io
importlib.reload(sys)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#改变标准输出的默认编码
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


'''此文档用于爬取https://cn.investing.com/crypto/currencies页面前100个虚拟币的相关参数，
初来乍到，请多指教'''

__version__ = 1.0

import requests
import json
import re


url_1 = 'https://cn.investing.com/crypto/currencies'


def get_html(url):

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    html = requests.get(url,headers=headers)
    if html.status_code == 200:
        htmltext = html.text
        return htmltext
    else:
        return 'none'


def parse_html():
    
    pattern = re.compile(
    r'i="\d{7}".*?title="(.*?)">.*?title="(.*?)">.*?href=.*?">(.*?)</a>.*?market.*?">(.*?)</td>.*?volume.*?">(.*?)</td>.*?vol">(.*?)</td>.*?24h.*?">(.*?)<.*?7d.*?">(.*?)</td>',re.S
    )
    html = get_html(url_1)
    items = re.findall(pattern,html)

    for item in items:
        yield{
            "name":item[0],
            "symbol":item[1],
            "price_dollar":item[2],
            "market_cap":item[3],
            "24h_volume":item[4],
            "total_vol":item[5],
            "change_24h":item[6],
            "change_7d":item[7],
        }


def output_print():
    for item in parse_html():
        print(item)


def init_file():
    item = 'This is the information of cryptocurrency'
    with open('cn.investing.com.text','w',encoding='utf-8') as f:
        f.write(json.dumps(item,ensure_ascii=False)+'\n')


def output_file():
    for item in parse_html():
        with open('cn.investing.com.text','a',encoding='utf-8') as f:
            f.write(json.dumps(item,ensure_ascii=False)+'\n')

if __name__ == '__main__':
    output_print()
    init_file()
    output_file()





