from appium import webdriver
from common.swipe import Swipe
# from appium.webdriver.common.touch_action import TouchAction
import  time
desired_caps = {'platformName': 'Android',
                'platformVersion': '7.0',
                'deviceName': '127.0.0.1:62001',
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                # 'automationName': 'Uiautomator2',
                'automationName': 'Appium',
                # 'unicodeKeyboard': True,
                # 'resetKeyboard': True,
                'noReset': True,
                # 'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
                'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'}
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(10)
Swipe.swipeDown(driver)
# def swipeDown(driver, t=500, n=1):
# l = driver.get_window_size()
# x1 = l['width'] * 0.5 # x坐标
# y1 = l['height'] * 0.25 # 起始y坐标
# y2 = l['height'] * 0.75 # 终点y坐标
# for i in range(n):
# driver.swipe(x1, y1, x1, y2,t)
# 向下滑动
# swipeDown(driver)
# 点开小程序
time.sleep(2)
driver.find_elements_by_id("com.tencent.mm:id/r9")[0].click()
time.sleep(4)
print(driver.contexts)
time.sleep(3)


