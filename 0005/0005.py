#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import os
filepath = 'images'


def get(filepath):
    filelist = []
    for f in os.listdir(filepath):
        filelist.append(f)
    print(filelist)
    return filelist


def change(filelist):
    os.chdir(filepath)
    for filename in filelist:
        im = Image.open(filename)
        w, h = im.size
        format = im.format
        while w > 640 or h > 1136:
            w *= 0.8
            h *= 0.8
        im.thumbnail((w, h))
        im.save(filename, format)
    print('over')

if __name__ == '__main__':
    change(get(filepath))
