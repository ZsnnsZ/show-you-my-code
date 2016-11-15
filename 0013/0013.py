#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import urllib
import urllib.request

base_url = 'http://tieba.baidu.com/p/2166231880'
pic_re = re.compile(r'"(http://imgsrc.*?)"')


def open_url(url, isByte=False):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    if isByte:
        return response.read()
    else:
        return response.read().decode('utf-8')


def get_all_picurl(data):
    return pic_re.findall(data)


def load_pic(picurl, picname):
    img = open_url(picurl, isByte=True)
    with open("pic/" + picname + '.jpg', 'wb') as f:
        f.write(img)

if __name__ == '__main__':
    data = open_url(base_url)
    allpicurl = get_all_picurl(data)
    for i in range(len(allpicurl)):
        load_pic(allpicurl[i], str(i))
    print('%s pictures have been downloaded' % len(allpicurl))
