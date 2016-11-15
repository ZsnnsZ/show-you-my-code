#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
filename = 'test.html'
body_re = re.compile(r'<body>[\s\S]*?</body>')


def print_body(filename):
    with open(filename, 'r') as f:
        data = f.read()
        body = body_re.findall(data)
    print(''.join(body))

if __name__ == '__main__':
    print_body(filename)
