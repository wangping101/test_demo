import requests
import urllib3
import json

urllib3.disable_warnings()

headers = {"Accept": "*/*",
           "Accept - Encoding": "br, gzip, deflate",
           "Accept - Language": "zh - cn",
           "Content - Length": "329",
           "Content - Type": "application/json; charset=UTF-8",
           "Referer": "https: // servicewechat.com / wx8290550a632226b3 / 0 / page - frame.html",
           "Connection": "keep - alive",
           "Host": "xiaowei.100bm.cn"}

payload = {"session_id": "d6fab768fdff7c9036587e980de3bdca",
           "activity_id": "81"}

url = 'https://xiaowei.100bm.cn/partner/act/detail?'

r1 = requests.post(url, data=payload, headers=headers, verify=False)

print(r1.json())

r3 = json.dumps(r1.json(), skipkeys=True, indent=2, allow_nan=False, separators=None, default=None, sort_keys=True)
print(r3)
