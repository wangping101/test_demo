#encoding: utf-8
import os
import unittest
import selenium
from appium import webdriver
from time import sleep
import warnings


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class xcxTests(unittest.TestCase):


    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)  #防止弹出警告
        #warnings.simplefilter(action='error', category=ResourceWarning)
        desired_caps = {}
        desired_caps['platformName'] = 'Android' #设备型号
        desired_caps['fastReset'] = 'false'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = '.ui.LauncherUI'
        desired_caps['fullReset'] = 'false'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['ChromeOptions']={'androidProcess': 'com.tencent.mm:tools'}
        #options = selenium.webdriver.ChromeOptions()
        #options.add_experimental_option('androidProcess', 'com.tencent.mm:tools')
        #desired_caps['ChromeOptions.CAPABILITY'] = 'options'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        print("aaaaaaaaaaaaaa1")
        self.driver.implicitly_wait(20)

        def tearDown(self):
            print("aaaaaaaaaaaaaa2")
            self.driver.quit()

    def test_order(self):
        self.driver.find_element_by_accessibility_id('搜索').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.tencent.mm:id/hz').send_keys(u"诚实充值特惠")
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.tencent.mm:id/lp').click()
        print(self.driver.contexts)
        self.driver.implicitly_wait(20)
        # time.sleep(2)
        self.driver.find_element_by_accessibility_id('10元').click()
        # time.sleep(2)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.tencent.mm:id/bri').send_keys('745520')
        self.driver.implicitly_wait(20)
        # is_fail = self.driver.find_element_by_name('支付密码错误，请重试').text
        is_success = self.driver.find_element_by_name('支付成功').get_attribute()
        print(is_success)
        for i in is_success:
            print(i.text)
        # 判断用户是否关注公众号
        if (u'完成' in i):
            print('未关注公众号')
        else:
            print('已关注公众号')

    def didibus_01(self):
        print("aaaaaaaaaaaaaa3")
        self.driver.find_element_by_accessibility_id(u"搜索").click()
        sleep(3)
        self.driver.find_element_by_id('com.tencent.mm:id/hz').send_keys(u"从零开始学自动化")
        sleep(3)
        self.driver.find_element_by_id('com.tencent.mm:id/lp').click()
        sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/acn').click()
        sleep(1)
        print(self.driver.contexts)
        #self.driver.switch_to.context('NATIVE_APP')
        sleep(1)
        self.driver.find_element_by_accessibility_id("app").click()
        sleep(10)
    def test_didibus_02(self):
        a=1
        b=2
        if a+b==2:
            print("True")
        else:
            print("False")
    def test_didbius_03(self):
        print("aaaaaaaaaaaa")







if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromTestCase(xcxTests)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    #unittest.xcxTests()
    unittest.main()






