# encoding: utf-8
import unittest
import warnings
from appium import webdriver
from common import logger
import time

# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )
logger = logger.Log()


class OrderTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        warnings.filterwarnings("ignore")
        logger.info('--启动设备--')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设备型号
        desired_caps['fastReset'] = 'false'
        desired_caps['noReset'] = 'false'
        desired_caps['deviceName'] = 'T8DDU15A28010857'  # 模拟器或真机链接号
        desired_caps['appPackage'] = 'com.tencent.mm'  # 包名
        desired_caps['appActivity'] = '.ui.LauncherUI'  # Activity名
        desired_caps['fullReset'] = 'false'
        desired_caps['unicodeKeyboard'] = 'True'  # 屏蔽手机输入法
        desired_caps['resetKeyboard'] = 'True'  # 屏蔽手机输入法
        desired_caps['autoAcceptAlerts'] = 'True'  # 支持断言
        # desired_caps['androidProcess'] = 'com.tencent.mm:tools'  # 公众号使用
        desired_caps['ChromeOptions'] = {'androidProcess': 'com.tencent.mm:appbrand0'}  # 小程序使用
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(30)

        cls.driver.find_element_by_accessibility_id('搜索').click()
        cls.driver.implicitly_wait(30)
        cls.driver.find_element_by_id('com.tencent.mm:id/hz').send_keys(u"诚实充值特惠")
        cls.driver.implicitly_wait(30)
        cls.driver.find_element_by_id('com.tencent.mm:id/lp').click()
        print(cls.driver.contexts)
        logger.info('--进入诚实充值特惠--')
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDown(cls):
        cls.tearDown()

    def test_order(self):
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_accessibility_id('请输入手机号码').send_keys('18280375357')
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_accessibility_id('10元').click()
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id('com.tencent.mm:id/bri').send_keys('745520')
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_name('支付成功')
            logger.info('--支付成功--')
        except:
            logger.warning('try未走通，密码错误或程序报错')


if __name__ == '__main__':
    unittest.main()
