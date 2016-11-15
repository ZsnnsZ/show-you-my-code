#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
filepath = 'article.txt'


def count_words(filepath):
    count = 0
    with open(filepath, 'r') as f:
        for line in f.readlines():
            words = re.findall(r'\w+', line)
            count += len(words)
        return count

if __name__ == '__main__':
    print('The number of words is: ' +
          str(count_words(filepath)))
