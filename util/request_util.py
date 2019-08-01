#!/usr/bin/env python
# -*- coding=utf-8 -*-
"""
网络请求工具类

Authors: shiwenli01@baidu.com
Date:    2019/08/01 上午11:34

"""

import requests
import urllib.parse


def net_ease_request(song_id, params, encSecKey):
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
        # 'Postman-Token':'4cbfd1e6-63bf-4136-a041-e2678695b419',
        "origin": 'https://music.163.com',
        # 'referer':'https://music.163.com/song?id=1372035522',
        'accept-encoding': 'gzip,deflate,br',
        'Accept': '*/*',
        'Host': 'music.163.com',
        'content-lenth': '472',
        'Cache-Control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive',
        # 'Cookie':'iuqxldmzr_=32; _ntes_nnid=a6f29f40998c88c693bc910331bd6bea,1558011234325; _ntes_nuid=a6f29f40998c88c693bc910331bd6bea; _ga=GA1.2.2120707788.1559308501; WM_TID=pV2C%2BjTrRwBBAAERUVJojniTwk8%2B8Zta; JSESSIONID-WYYY=nvf%2BggodQRfcT%2BTvBRmANqMrsDeQCxRvqwFsxDr3eJvNNWhGYFhfCXKFkfAfOdbHhpCsMzT39mAeJ7ZamBQZbiwwtnSZD%5CPWRqKxD9t6dGKD3bTVjomjgB39DB07RNIWI32bYKa2H4fg1qQgqI%2FR%2B%2Br%2BZXJvgFg1Vh%2FA2XRj9S4p0EMu%3A1560927288799; WM_NI=DthwcEQf5Ew2NbTIZmSNhSnm%2F8VWsg5RxhkYogvs2luEwZ6m5UhdzbHYPIr654ZBWKV4o22%2BEwb9BvdLS%2BFOmOAEUG%2B8xd8az4CX%2FiAL%2BZkz3syA0onCPkhQwCtL4pkUcjg%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed2d650989c9cd1dc4bb6b88eb2c84e979f9aaff773afb6fb83d950bcb19ecce92af0fea7c3b92a88aca898e24f93bafba6f63a8ebe9caad9679192a8b4ed67ede89ab8f26df78eb889ea53adb9ba94b168b79bb9bbb567f78ba885f96a8c87a0aaf13ef7ec96a3d64196eca1d3b12187a9aedac17ea8949dccc545af918fa6d84de9e8b885bb6bbaec8db9ae638394e5bbea72f1adb7a2b365ae9da08ceb5bb59dbcadb77ca98bad8be637e2a3'
    }
    url2 = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_" + song_id + "?csrf_token="
    fromdata = {
        "params": params,
        "encSecKey": encSecKey,
    }

    fromdata = urllib.parse.urlencode(fromdata).encode('utf-8')
    req = requests.post(url=url2, data=fromdata, headers=header, )
    res = req.text;
    print(url2)
    print(req.status_code)
    print(res)
    return req.json()


if __name__ == '__main__':
    song_id = '553398526'
    params = "FyKC+C/i0BrPR6Xh6bellvcdymVcyYL8kMx9hiMmeq+UMN9RCgDltULQBT0aEMo/ukPnRbDVlFLzz4+uz3JITMGnHw0QtZzunaElHvXr8sSIrPVfpfjCTO6bbpGXNV8T4qEnDriY9Vx7k/nbQV+NS+ZIlSgjwEzcdLoFFGT+YncrQhfMHQtbRnkYR+MaHxSK"
    encSecKey = "b0fa7e7aeb1cb336c82e467a119ec1690e0a81134f13f603c49ab626454074e0ced5fdb95e6212a1721f9484b92521d3352408c48919996f201557349c1a3d413a3f3c5decfdac37a3475ddb2461daff073464b4e8a81d3203858b24f7a0ace449e57b460e8cd228d2516710876f52bc7d985f792bd3785f2f415b0c298b3be6"

    net_ease_request(song_id, params, encSecKey)
    pass
