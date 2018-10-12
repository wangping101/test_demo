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
payload = {"session_id": "53988cb8508177a24a05be45291960fd",
           "order_no": "TH18091317280969345",
           "id_face_photo_url": "http://192.168.106.211:8100/image/b065aee1954e3ef71c874bc4c44d13c7.jpg",
           "id_back_photo_url": "http://192.168.106.211:8100/image/b065aee1954e3ef71c874bc4c44d13c7.jpg",
           "user_face_photo_url": "http://192.168.106.211:8100/image/b065aee1954e3ef71c874bc4c44d13c7.jpg"}
payload1 = {"name": "http://192.168.106.211:8100/image/b065aee1954e3ef71c874bc4c44d13c7.jpg"}
payload3 = {"session_id": "53988cb8508177a24a05be45291960fd"}

url = 'https://xiaowei.100bm.cn/kingcard/update/id/info?'
url1 = 'https://xiaowei.100bm.cn/sys/file/upload?'
url3 = 'https://xiaowei.100bm.cn/order/adoc/list?'

r = requests.post(url, data=payload, headers=headers, verify=False)
print(json.dumps(r.json(), indent=2, ensure_ascii=False))

r1 = requests.post(url1, data=payload1, headers=headers, verify=False)
rr = json.dumps(r1.json(), indent=2, ensure_ascii=False)
print(rr)

r3 = requests.post(url3, data=payload3, headers=headers)
r6 = json.dumps(r3.json(), indent=2, ensure_ascii=False)
print(r6)
