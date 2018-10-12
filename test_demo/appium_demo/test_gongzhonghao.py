# coding=utf-8
from appium import webdriver
import json
import time

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'T8DDU15A28010857',  # T8DDU15A28010857 #127.0.0.1:62001
    'platformVersion': '4.4.2',
    # apk包名
    'appPackage': 'com.tencent.mm',
    # apk的launcherActivity
    'appActivity': '.ui.LauncherUI',
    'noReset': 'true',
    'unicodeKeyboard': 'True',
    'resetKeyboard': 'True',
    'chromOptions': {'androidProcess': 'com.tencent.mm:tools'
                     # 'chromOptions':{'androidProcess':'com.tencent.mm:appbrand0'

                     }}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
driver.find_element_by_accessibility_id('搜索').click()
driver.implicitly_wait(10)
driver.find_element_by_id('com.tencent.mm:id/hz').send_keys(u"从零开始学自动化")
driver.implicitly_wait(10)

driver.find_element_by_id('com.tencent.mm:id/lp').click()
driver.implicitly_wait(10)
driver.find_element_by_id('com.tencent.mm:id/acn').click()
driver.implicitly_wait(10)
driver.find_element_by_accessibility_id('app').click()
app = driver.page_source
print(app)
# print(driver.contexts)
driver.quit()
