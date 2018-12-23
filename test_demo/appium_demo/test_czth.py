import unittest
import warnings
from appium import webdriver
from common.Logger import Log
import time

logger = Log()


class orderTests(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # 启动微信程序
        logger.info('--启动微信程序--')
        warnings.filterwarnings("ignore")  # 禁用警告提示
        desired_caps = {}  # appium参数设置
        desired_caps['platformName'] = 'Android'
        desired_caps['fastReset'] = 'false'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = '.ui.LauncherUI'
        desired_caps['fullReset'] = 'false'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['autoAcceptAlerts'] = 'True'  # 支持断言
        desired_caps['ChromeOptions'] = {'androidProcess': 'com.tencent.mm:appbrand0'}  # 小程序使用
        desired_caps['ChromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}  # 公众号使用
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(30)
        cls.driver.find_element_by_accessibility_id('搜索').click()
        cls.driver.implicitly_wait(30)
        cls.driver.find_element_by_id('com.tencent.mm:id/hz').send_keys(u"诚实充值特惠")
        cls.driver.implicitly_wait(30)
        cls.driver.find_element_by_id('com.tencent.mm:id/lp').click()
        logger.info('--成功进入诚实充值特惠小程序--')
        print(cls.driver.contexts)

    def test_order_01(self):
        logger.info('--下10元话费订单--')
        try:
            self.driver.implicitly_wait(50)
            self.driver.find_element_by_accessibility_id('10元').click()
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id('com.tencent.mm:id/bri').send_keys('000021')
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_name('支付成功')
            logger.info('--下单成功--')
        except Exception as e:
            logger.warning('--下单失败--')
            print("出错了" + str(e))

    @classmethod
    def tearDown(cls):
        time.sleep(10)
        cls.driver.quit()
        logger.info('--退出程序--')


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(orderTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
