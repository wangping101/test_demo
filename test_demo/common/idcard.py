#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: _wapn
import requests
import re

# 身份证号生成
url = 'http://sfz.diqibu.com/?'
payload = {'region': '513721',
           'birthday': '19900307',
           'sex': '1',
           'num': '1'}


class Card:
    def idcard(self):
        r = requests.get(url, params=payload)
        e = '\d{17}[\d|X|x]'
        x = re.findall(e, r.text)
        for i in x:
            return i


if __name__ == '__main__':
    Card().idcard()
    print(Card().idcard())
