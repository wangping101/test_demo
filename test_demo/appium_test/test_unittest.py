#encoding: utf-8
import os
import unittest
import selenium
from appium import webdriver
from time import sleep


#PATH = lambda p: os.path.abspath(
    #os.path.join(os.path.dirname(__file__)[0], p)
#)

class xcxTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android' #设备型号
        desired_caps['platformVersion']='7.0'
        #desired_caps['fastReset'] = 'true'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = '.ui.LauncherUI'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['noReset']='True'
        desired_caps['fullReset'] = 'false'
        #options = selenium.webdriver.ChromeOptions()
        #options.add_experimental_option('androidProcess', 'com.tencent.mm:tools')
        #desired_caps['ChromeOptions.CAPABILITY'] = 'options'

        desired_caps['chromeOptions']= {'androidProcess': 'com.tencent.mm:appbrand0'}

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


    def tearDown(self):
        self.driver.quit()

    def test_didibus(self):
        #os.popen('adb shell ime set com.meizu.flyme.input/com.meizu.input.MzInputService')
        #os.popen('adb shell input keyevent 66')
        #sleep(5)
        #print(self.driver.contexts)
        #self.driver.switch_to.context(u'WEBVIEW_com.tencent.mm:tools')
        #self.driver.find_element_by_class_name('search_item_inner').click()
        self.driver.find_element_by_accessibility_id("搜索").click()
        sleep(3)
        self.driver.find_element_by_id('com.tencent.mm:id/hz').send_keys("chongzhitehui")
        sleep(3)
        self.driver.find_element_by_id('com.tencent.mm:id/lp').click()
        sleep(3)
        print(self.driver.contexts)
        self.driver.switch_to.context(u'WEBVIEW_com.tencent.mm:tools')
        sleep(5)
        self.driver.find_element_by_accessibility_id("流量").click()
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(xcxTests)
    unittest.TextTestRunner(verbosity=2).run(suite)


