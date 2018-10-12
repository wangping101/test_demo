#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: _wapn
import redis

# 链接redis
r = redis.StrictRedis(host='192.168.0.116', port=6379, db=0)
t = r.keys('th:{th_week}*')  # 找出以xxx开头的所有key
for i in t:
    r.delete(i)
