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
        temp_list = []
        print_flag = False
        # del blanks
        for c in input_line:
            if c != ' ':
                temp_list.append(c)
        # for each character in input_line,we should do this to avoid situation
        # like 'sesex'
        for i in range(len(temp_list)):
            for j in range(len(words_list)):
                # when a character appears in filtered-word,begin to match the
                # rest
                if temp_list[i] in words_list[j]:
                    for k in range(len(words_list[j])):
                        if temp_list[i + k] != words_list[j][k]:
                            break
                        # only when the whole word matchs filtered-word, can it
                        # be replaced
                        elif k == len(words_list[j]) - 1:
                            for k in range(len(words_list[j])):
                                temp_list[i + k] = '*'
                            print_flag = True
                else:
                    continue
        # if there is no filtered-word in input_line,print the original
        # input_line
        if print_flag:
            print ("".join(temp_list))
        else:
            print (input_line)
