#encoding: utf-8
import os
import unittest
import selenium
import warnings
import json
from appium import webdriver
import  time

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class orderTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.filterwarnings("ignore")
        desired_caps = {}
        desired_caps['platformName'] = 'Android' #设备型号
        desired_caps['fastReset'] = 'false'
        desired_caps['deviceName'] = 'T8DDU15A28010857'
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = '.ui.LauncherUI'
        desired_caps['fullReset'] = 'false'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['autoAcceptAlerts'] = 'True' #支持断言
        desired_caps['ChromeOptions']={'androidProcess': 'com.tencent.mm:appbrand0'}
        #options = selenium.webdriver.ChromeOptions()
        #options.add_experimental_option('androidProcess', 'com.tencent.mm:tools')
        #desired_caps['ChromeOptions.CAPABILITY'] = 'options'
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(30)
        cls.driver.find_element_by_accessibility_id('搜索').click()
        cls.driver.implicitly_wait(30)
        cls.driver.find_element_by_id('com.tencent.mm:id/hz').send_keys(u"诚实充值特惠")
        cls.driver.implicitly_wait(30)
        cls.driver.find_element_by_id('com.tencent.mm:id/lp').click()
        print(cls.driver.contexts)
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @unittest.skip  # 无条件跳过
    def test_order(self):
        print("aaaaaaaaaaa1")
        self.driver.implicitly_wait(10)
        try:
            self.driver.implicitly_wait(20)
            # time.sleep(2)
            self.driver.find_element_by_accessibility_id('10元').click()
            # time.sleep(2)
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id('com.tencent.mm:id/bri').send_keys('635881')
            self.driver.implicitly_wait(20)
            apps = self.driver.find_element_by_name('支付成功').get_attribute('name')
            time.sleep(10)
            for i in apps:
                print(i.name)
            if '充值特惠' in i.name:
                print("未关注公众号")
            # 在支付成功页面找元素，判断是否支付成功，是否关注公众号
            if (self.driver.find_element_by_id(u'com.tencent.mm:id/dxg')):
                print('支付成功')
            try:
                if (self.driver.find_element_by_name(u'充值特惠')):
                    print(u'未关注充值特惠')
            except:
                print('try未走通，已关注公众号')
        except:
            print('try未走通，密码错误或程序报错')

    @unittest.skipUnless(condition='False', reason=u'为False不执行')  # 为False时跳过
    def test_didibus_02(self):
        print("aaaaaaaaaaaaa2")
        a=1
        b=2
        if a+b==2:
            print("True")
        else:
            print("False")

    @unittest.skipIf(condition='True', reason=u'为Ture时跳过')
    def test_didbius_03(self):
        print("aaaaaaaaaaaaa3")
        a=1
        b=2
        if a+b==2:
            print("True")
        else:
            print("False")

    @unittest.expectedFailure  # 断言跳过
    def test_didbius_04(self):
        print("aaaaaaaaaaaaaa4")
        a = 5
        b = 8
        self.assertEquals(a, b)

if __name__=="__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(orderTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()







