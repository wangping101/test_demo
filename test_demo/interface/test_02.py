import requests
import urllib3

urllib3.disable_warnings()

headers = {"Accept": "*/*",
           "Accept - Encoding": "br, gzip, deflate",
           "Accept - Language": "zh - cn",
           "Content - Length": "329",
           "Content - Type": "application/json; charset=UTF-8",
           "Referer": "https: // servicewechat.com / wx8290550a632226b3 / 0 / page - frame.html",
           "Connection": "keep - alive",
           "Host": "xiaowei.100bm.cn"}

r = requests.get('http://192.168.5.91:5000/delete/userdata?user_id=2835', headers=headers, verify=False)

print(r.status_code)
