from selenium import webdriver
import unittest
import json
import re
from  selenium.webdriver.common.action_chains import ActionChains #导入鼠标模块
from  selenium.webdriver.common.keys import Keys  #导入键盘模块
def setup():
    pass
def login():
    option = webdriver.ChromeOptions()
# 伪装iphone登录
# option.add_argument('--user-agent=iphone')
# 伪装android
    option.add_argument('--user-agent=android')
    driver = webdriver.Chrome(chrome_options=option)
    driver.get('http://www.taobao.com/')
    app = driver.page_source
    print(app)
def teardown():
    pass
if __name__=='__main()__':
    unittest.main()




