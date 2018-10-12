from common.Oracle import OracleUtil
import requests
import urllib3

urllib3.disable_warnings()
headers =  {"Accept": "*/*",
            "Accept - Encoding": "br, gzip, deflate",
            "Accept - Language": "zh - cn",
            "Content - Length": "329",
            "Content - Type": "application / x - www - form - urlencoded",
            "Referer": "https: // servicewechat.com / wx8290550a632226b3 / 0 / page - frame.html",
            "Connection": "keep - alive",
            "Host": "xiaowei.100bm.cn"}


url1 = 'https://xiaowei.100bm.cn/order/wx/payment/notify?'
url2 = "https://xiaowei.100bm.cn/order/wx/user/request?"
payload1 = {
        "order_amount": "1",
        "order_id": "3688812",
        "appid": "wx8290550a632226b3",
        "payer_openid": "oOMYa0bGLnzaki4NEDjnhSKk822A",
        "pay_status": "SUCCESS",
        "plat_order_no": "4200000068201803233892242595"}
payload2 = {
        "business_type": "1000000",
        "order_type": "1",
        "product_no": "2455",
        "recharge_account": "18280375357",
        "session_id": "da624cc2edc11e7efbc5a5eee1163224",
        "sign": "f20c0feffefaa84365f00216af0b908f",
        "form_id": "22cdb7c846702bca453a0fc12b78ba76",
        "app_version": "v5.0.63",
        "order_source": "0"}

for i in range(1, 5):
    i += 1
    if i % 2 == 0:
        r = requests.post(url2, data=payload2, headers=headers, verify=False)
        print(r.text)
# --------数据库中读取数据-----------------
    else:
        sql = 'select t.order_no,t.pay_amount from th_order_info t where t.order_status =10 and t.user_id =2697 '
        r1 = OracleUtil().oracle_getrows(sql)
        r2 = ('ext_order_no', 'pay_amount')
        for i in r1:
            r3 = dict(zip(r2, i))
            payload1['ext_order_no'] = r3['ext_order_no']
            payload1['pay_amount'] = int(r3['pay_amount'] * 100)
            print(payload1)
            r = requests.post(url1, data=payload1, headers=headers)
            print(r.text)








