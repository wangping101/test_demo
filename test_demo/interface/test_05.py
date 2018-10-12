#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: _wapn
from common.idcard import Card
from common.Excel import ExcelUtil
import requests, urllib3, json, random, os

urllib3.disable_warnings()
base_url = 'https://xiaowei.100bm.cn'
headers = {"Accept": "*/*",
           "Accept - Encoding": "br, gzip, deflate",
           "Accept - Language": "zh - cn",
           "Content - Length": "329",
           "Content - Type": "application/json; charset=UTF-8",
           "Referer": "https: // servicewechat.com / wx8290550a632226b3 / 0 / page - frame.html",
           "Connection": "keep - alive",
           "Host": "xiaowei.100bm.cn"}
url = '/order/ydcard/request?'

# 获取Excel表数据
filePath = os.path.abspath('..\Excel\\Excel1.xlsx')  # 相对路径
# filePath = "F:\\test_demo\\Excel\\Excel1.xlsx" # 绝对路径
sheetName = "Sheet1"
data = ExcelUtil(filePath, sheetName).dict_data()
# 创建订单
for i in range(10):
    # rr = random.sample(data, 1)   # 从列表中随机选择1个元素(可设置)，仍是列表
    payload2 = random.choice(data)  # 从列表中随机选出某个元素，仅选出元素
    payload2['session_id'] = '7b00177c094b33c06cb735ce148d5c69'
    payload2['product_name'] = 58
    # 调用接口获取身份证号码
    idcard = Card().idcard()
    payload2['id_no'] = idcard
    r = requests.post(url=base_url + url, data=payload2, headers=headers)
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
