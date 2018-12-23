from time import sleep
from appium import webdriver

desired_caps = {
        'platformName': 'Android',
        'platformVersion': '4.4.2',
        'deviceName': '127.0.0.1:62001',
        'appPackage': 'com.baidu.yuedu',
        'appActivity': 'com.baidu.yuedu.splash.SplashActivity',
        # 'fullReset': 'false',
        # 'unicodeKeyboard': 'ture', #屏蔽软键盘，使用unicode编码方式发送字符串
        # 'resetKeyboard': 'ture',   #屏蔽软键盘，将键盘隐藏起来
        }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 获取屏幕的size
size = driver.get_window_size()
print(size)
# 获取width
print(size['width'])
# 获取height
print(size['height'])

sleep(15)
driver.find_element_by_id("com.baidu.yuedu:id/cb_choose_view").click()
driver.find_element_by_id("com.baidu.yuedu:id/cb_choose_book").click()
driver.find_element_by_id("com.baidu.yuedu:id/tv_confirm_button").click()
sleep(10)
# 点图书按钮
driver.find_element_by_id("com.baidu.yuedu:id/righttitle").click()
sleep(10)
# 获取图书界面所有环境
contexts = driver.contexts
print(contexts)
# 切换到webview
driver.switch_to.context(contexts[1])
# 获取当前环境，是否切换成功
now = driver.current_context
print(now)
# 切回native
driver.switch_to.context(contexts[0])
# driver.switch_to.context("NATIVE_APP") # 这样也是可以的
# 获取当前的环境，看是否切换成功
now = driver.current_context
print(now)
