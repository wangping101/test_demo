#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: _wapn
import requests
import re
import random

# 身份证号生成
url = 'http://sfz.diqibu.com/?'
payload = {'region': '513721',
           'birthday': '19900307',
           'sex': '1',
           'num': '5'}
# sexs = [1, 2]
# b = []
# for i in range(19900102, 19900106):
#     b.append(i)
# oo = '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$'
#
# # ee = '(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))'
# ee = '(\d{4}(01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1]))'
# x = str(b)



class Card:
    def idcard(self):
        # payload['sex'] = random.choice(sexs)
        # payload['birthday'] = random.choice(rr)
        r = requests.get(url, params=payload)
        # print(r.text)
        e = '\d{17}[\d|X|x]'
        x = re.findall(e, r.text)
        for i in x:
            return i


if __name__ == '__main__':
    Card().idcard()
    print(Card().idcard())
