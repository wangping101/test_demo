# encoding: utf-8
import os
import unittest
import selenium
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class xcxTests(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设备型号
        desired_caps['fastReset'] = 'false'
        desired_caps['fastReset'] = 'false'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = '.ui.LauncherUI'
        desired_caps['fullReset'] = 'false'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['androidProcess'] = 'com.tencent.mm:tools'  # 公众号使用
        # desired_caps['androidProcess'] = 'com.tencent.mm:appbrand0' #小程序使用

        # options = selenium.webdriver.ChromeOptions()
        # options.add_experimental_option('androidProcess', 'com.tencent.mm:tools')
        # desired_caps['ChromeOptions.CAPABILITY'] = 'options'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(20)

    def tearDown(self):
        self.driver.quit()

    def test_didibus(self):
        self.driver.find_element_by_name('发现').click()
        self.driver.find_element_by_name('小程序').click()
        # self.driver.find_element_by_name('搜索').click()
        sleep(5)
        self.driver.find_element_by_class_name('android.widget.TextView').click()  # send_keys('诚实充值特惠')
        os.popen('adb shell ime set com.meizu.flyme.input/com.meizu.input.MzInputService')
        self.driver.find_element_by_class_name('android.widget.EditText').click()
        os.popen('adb shell input keyevent 66')
        sleep(5)
        print(self.driver.contexts)
        self.driver.switch_to.context(u'WEBVIEW_com.tencent.mm:tools')
        self.driver.find_element_by_class_name('search_item_inner').click()


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(xcxTests)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
