#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: _wapn
import hashlib
import hmac

# md5加密
hash2 = hashlib.md5()
hash2.update('123456'.encode('Utf-8'))
print(hash2.hexdigest())

# sha系列加密
hash1 = hashlib.sha256()
hash1.update('123456'.encode('utf-8'))
print(hash1.hexdigest())

# hmac加密，hmac内部对创建的key和内容进行处理后再加密
h = hmac.new('加密'.encode('utf-8'))
h.update(input('>>>:').encode('utf-8'))
print(h.hexdigest())
