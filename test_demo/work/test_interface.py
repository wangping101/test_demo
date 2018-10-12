import requests
import json
import urllib3
import time
import unittest


urllib3.disable_warnings()

headers =  {"Accept": "*/*",
            "Accept - Encoding": "br, gzip, deflate",
            "Accept - Language": "zh - cn",
            "Content - Length": "329",
            "Content - Type": "application / x - www - form - urlencoded",
            "Referer": "https: // servicewechat.com / wx8290550a632226b3 / 0 / page - frame.html",
            "Connection": "keep - alive",
            "Host": "xiaowei.100bm.cn"}

url1 = "https://xiaowei.100bm.cn/banner/list/query?"               # banner信息接口
url2 = "https://xiaowei.100bm.cn/partner/act/list?"                # 查询合作商活动列表
url3 = "https://xiaowei.100bm.cn/partner/act/detail?"              # 活动详情
url4 = "https://xiaowei.100bm.cn/partner/act/join?"                # 用户参加活动
url5 = "https://xiaowei.100bm.cn/partner/act/my/list?"             # 我的活动列表
url6 = "https://xiaowei.100bm.cn/partner/act/record/contactinfo?"  # 记录赞助商联系信息
url7 = "https://xiaowei.100bm.cn/partner/act/record/receiveinfo?"  # 记录用户领奖地址

payload1 = {
        "session_id": "da624cc2edc11e7efbc5a5eee1163224",
        "tag": "partnet_act"}

payload2 = {
        "session_id": "da624cc2edc11e7efbc5a5eee1163224",
        "tag": "partnet_act",
        "ps": "10",
        "pi": "1"}

payload3 = {
        "session_id": "da624cc2edc11e7efbc5a5eee1163224",
        "tag": "partnet_act",
        "activity_id": "2"}

payload4 = {
        "session_id": "da624cc2edc11e7efbc5a5eee1163224",
        "tag": "partnet_act",
        "activity_id": "1"}
payload5 = {
        "session_id": "da624cc2edc11e7efbc5a5eee1163224",
        "tag": "partnet_act"}

payload6 = {
        "session_id": "da624cc2edc11e7efbc5a5eee1163224",
        "tag": "partnet_act",
        "conact_name": "wapn",                # 姓名不可为空
        "conact_phone": "18280375357",        # 手机号不可为空
        "promotion_content": "11"}             # 推广内容不少于10字

payload7 = {
        "session_id": "da624cc2edc11e7efbc5a5eee1163224",
        "tag": "partnet_act",
        "activity_id": "1",
        "receive_user_name": "wapn",
        "receive_user_mobile": "18280375357",
        "receive_user_addr": "0121111111111"}
class Interface(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

# 查询banner信息
    def test_01(self):
        a1 = requests.post(url1, data=payload1, headers=headers)
        a2 = a1.text
        a3 = eval(a2)  # 将字符转换成字典， 也可用r3 = exec(r2)
        a4 = json.dumps(a3, indent=2, ensure_ascii=False)
        print(u"查询banner信息", a4)
    def test_02(self):
# 查询合作商活动列表
        a1 = requests.post(url2, data=payload2, headers=headers)
        a2 = a1.text
        a3 = eval(a2)
        a4 = json.dumps(a3, indent=2, ensure_ascii=False)
        print(u"查询合作商活动列表", a4)
    def test_03(self):
# 活动详情
        a1 = requests.post(url3, data=payload3, headers=headers)
        a2 = a1.text
        a3 = eval(a2)
        a4 = json.dumps(a3, indent=2, ensure_ascii=False)
        print(u"活动详情", a4)
# 用户参加活动
    def test_04(self):
        a1 = requests.post(url4, data=payload4, headers=headers)
        a2 = a1.text
        a3 = eval(a2)
        a4 = json.dumps(a3, indent=2, ensure_ascii=False)
        print(u"用户参加活动", a4)

# 我的活动列表
    def test_05(self):
        a1 = requests.post(url5, data=payload5, headers=headers)
        a2 = a1.text
        a3 = eval(a2)
        a4 = json.dumps(a3, indent=2, ensure_ascii=False)
        print(u"我的活动列表", a4)

#  记录赞助商联系信息
    def test_06(self):
        a1 = requests.post(url6, data=payload6, headers=headers)
        a2 = a1.text
        a3 = eval(a2)
        a4 = json.dumps(a3, indent=2, ensure_ascii=False)
        print(u"记录赞助商联系信息", a4)
# 记录用户领奖地址
    def test_07(self):
        a1 = requests.post(url7, data=payload7, headers=headers)
        a2 = a1.text
        a3 = eval(a2)
        a4 = json.dumps(a3, indent=2, ensure_ascii=False)
        print(u"记录用户领奖地址", a4)
        time.sleep(2)

