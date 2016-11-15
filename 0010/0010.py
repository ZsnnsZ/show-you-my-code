#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string
base = string.ascii_letters + string.digits


def randWord():
    return random.choice(base)


def randColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def randColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def createPic():
    width = 240
    height = 60
    im = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建font对象:
    font = ImageFont.truetype('arial.ttf', 35)
    # 创建draw对象:
    draw = ImageDraw.Draw(im)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=randColor())
    # 输出文字:
    for t in range(4):
        draw.text((60 * t + 10, 10), randWord(), font=font, fill=randColor2())
    # 模糊处理
    im = im.filter(ImageFilter.BLUR)
    im.show()
    im.save('code.jpg', 'jpeg')

if __name__ == '__main__':
    createPic()
