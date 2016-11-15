#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filename = 'filtered_words.txt'


def get_words(filename):
    words_list = []
    with open(filename, 'r', encoding='gbk') as f:
        data = f.read()
        words_list = data.split('\n')
    return words_list

if __name__ == '__main__':
    words_list = get_words(filename)
    while True:
        input_line = input('>')
        # temp_str = str(input_line)
        # temp_list = temp_str.split(' ')
        temp_list = input_line.split(' ')
        temp_list2 = []
        # del ''
        for i in range(len(temp_list)):
            if temp_list[i] != '':
                temp_list2.append(temp_list[i])

        for i in range(len(temp_list2)):
            if temp_list2[i] in words_list:
                temp_list2[i] = 'Freedom'
            else:
                temp_list2[i] = 'Human Rights'

        print (" ".join(temp_list2))
