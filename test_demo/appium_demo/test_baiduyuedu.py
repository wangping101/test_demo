# coding:utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'T8DDU15A28010857',
    'platformVersion': '4.4.2',
    'appPackage': 'com.baidu.yuedu',
    'appActivity': 'com.baidu.yuedu.splash.SplashActivity',
    'noReset': 'true',
    'automationName': 'Uiautomator2'
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 等主页面activity出现
driver.wait_activity(".base.ui.MainActivity", 10)
driver.back()   #返回
# 定位toast元素
toast_loc = ("xpath", ".//*[contains(@text,'再按一次退出')]")
t = WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located(toast_loc))
print(t)

