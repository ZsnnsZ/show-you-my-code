#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector


def store_mysql(filepath):
    conn = mysql.connector.connect(
        user='root', password='177288', database='test')
    cursor = conn.cursor()

    # 判断表是否已经存在
    cursor.execute('show tables in test;')
    tables = cursor.fetchall()
    findtables = False
    for table in tables:
        if 'coupon' in table:
            findtables = True
    if not findtables:
        cursor.execute('''
                CREATE TABLE `test`.`coupon` (
                `id` INT NOT NULL AUTO_INCREMENT,
                `coupon` VARCHAR(255) NOT NULL,
                PRIMARY KEY (`id`));
        ''')

    f = open(filepath, 'rb')
    for line in f.readlines():
        coupon = line.strip()
        cursor.execute(
            "insert into test.coupon (coupon) values(%s);", [coupon])

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    store_mysql('coupons.txt')
