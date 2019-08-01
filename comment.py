#!/usr/bin/env python
# -*- coding=utf-8 -*-
"""
网络请求工具类

Authors: shiwenli01@baidu.com
Date:    2019/08/01 上午11:34

"""

import requests
import urllib.parse
import requests
import urllib.parse
from wordcloud import WordCloud
import jieba.analyse
import matplotlib.pyplot as plt

from util import request_util
from util import AES_encrypt_util


def getcomment(songid, page):
    encSecKey = "c81160c64a08feb6cfed91c1619d5bffd05dd278b685c94a748689edf035ee0436b66aa7019927ce0fedd26aee9a22cdc6743e58a120f9db0126ebb2e61dae3f7ee21088eb747f829bceed9a5bbb9ee7a2eecf1a358feac431acaab17c95b8491a6a955f7c17a02a3e7886390c2cb3b981f4ccbd5163a566d27ace95db073401"

    aes_key = '0CoJUm6Qyw8W8jud'  ## 不变的
    print('aes_key:' + aes_key)
    # 对英文加密
    source_en = '{"rid":"R_SO_4_' + songid + '","offset":"' + str(
        page * 20) + '","total":"false","limit":"20","csrf_token":""}'

    # offset自己该
    print(source_en)
    encrypt_en = AES_encrypt_util.encrypt(aes_key, source_en)  # 第一次加密
    print(encrypt_en)
    aes_key = '3Unu7SzdXGctW1vA'
    encrypt_en = AES_encrypt_util.encrypt(aes_key, str(encrypt_en))  # 第二次加密
    print(encrypt_en)
    params = encrypt_en
    print(params)
    return request_util.net_ease_request(songid, params, encSecKey)


if __name__ == '__main__':
    songid = '346576'
    page = 0
    text = ''
    for page in range(10):
        comment = getcomment(songid, page)
        comment = comment['comments']
        for va in comment:
            print(va['content'])
            text += va['content']
    ags = jieba.analyse.extract_tags(text, topK=50)  # jieba分词关键词提取，40个
    print(ags)
    text = " ".join(ags)
    backgroud_Image = plt.imread('tt.jpg')  # 如果需要个性化词云
    wc = WordCloud(background_color="white",
                   width=1200, height=900,
                   mask=backgroud_Image,  # 设置背景图片

                   # min_font_size=50,
                   font_path="simhei.ttf",
                   max_font_size=200,  # 设置字体最大值
                   random_state=50,  # 设置有多少种随机生成状态，即有多少种配色方案
                   )  # 字体这里有个坑，一定要设这个参数。否则会显示一堆小方框wc.font_path="simhei.ttf"   # 黑体
    # wc.font_path="simhei.ttf"
    my_wordcloud = wc.generate(text)
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()  # 如果展示的话需要一个个点
    file = 'image/' + str("aita") + '.png'
    wc.to_file(file)
