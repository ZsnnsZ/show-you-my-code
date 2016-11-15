#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
filename = 'test.html'
body_re = re.compile(r'"((https|ftps|http|ftp)://.*?)"')


def print_url(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
        body = body_re.findall(data)
    print(body)

if __name__ == '__main__':
    print_url(filename)
