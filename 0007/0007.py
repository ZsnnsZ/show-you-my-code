#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
filepath = 'code'


def get(filepath):
    filelist = []
    for f in os.listdir(filepath):
        filelist.append(f)
    print(filelist)
    return filelist


def count(filelist):
    os.chdir(filepath)
    code_total = 0
    blank_total = 0
    note_total = 0
    for filename in filelist:
        code, blank, note = 0, 0, 0
        note_flag = False
        with open(filename, 'r') as f:
            for line in f.readlines():
                code += 1
                if (line.strip().startswith('\"\"\"') or line.strip().startswith('\'\'\'')) and not note_flag:
                    note_flag = True
                    note += 1
                    continue

                if line.strip().startswith('\"\"\"') or line.strip().startswith('\'\'\''):
                    note_flag = False
                    note += 1

                if line == '\r\n' or line == '\n':
                    blank += 1

                if line.strip().startswith('#') or note_flag:
                    note += 1

        code_total += code
        blank_total += blank
        note_total += note
        print(u"在 %s 文件中，共有 %s 行代码，空白行有 %s 行，注释行有 %s 行\n" %
              (filename, code, blank, note))
    print(u"所有文件共有 %s 行代码，空白行有 %s 行，注释行有 %s 行\n" %
          (code_total, blank_total, note_total))

if __name__ == '__main__':
    count(get(filepath))
