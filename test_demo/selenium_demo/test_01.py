from selenium import webdriver
from common.Excel import ExcelUtil
from common.logger import Log
import ddt
import unittest
import time

filePath = "F:\\test_demo\\Excel\\Excel.xlsx"
sheetName = "Sheet1"
test_data = ExcelUtil(filePath, sheetName).dict_data()
print(test_data)

# testdata = [{"username":"admin","psw":"123456"}]
logger = Log()


@ddt.ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUp(cls):
        logger.info('测试开始')
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://192.168.106.211:8100/")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDown(cls):
        logger.info('测试结束')
        pass

    @ddt.data(*test_data)
    def test_add_01(self, data):
        logger.info('获取登录账号')
        print("测试数据%s" % data)
        # 调用登录方法
        self.login(data['username'], data['psw'])
        logger.info('添加商品')
        try:
            self.driver.find_element_by_class_name('text_select').click()
            self.driver.find_element_by_xpath("//button[@type='button']").click()
            s = self.driver.find_element_by_name('partner_id')
            s.find_element_by_class_name('ng-star-inserted').click()
            self.driver.find_element_by_name('sort').send_keys('1')
            self.driver.find_element_by_name('partner_summary').send_keys(u'商家简介')
            self.driver.find_element_by_name('start_time').send_keys('2018-09-07 00:00:00')
            self.driver.find_element_by_name('end_time').send_keys('2018-09-15 00:00:00')
            self.driver.find_element_by_name('prize_name').send_keys('手机')
            self.driver.find_element_by_name('prize_img').send_keys('http://192.168.106.211:8100/image/5038c3c0d1ab63b58bfc764b5ae98cf4.png')
            s1 = self.driver.find_element_by_name('prize_open_type')
            s1.find_element_by_xpath("//option[@value=2]").click()
            self.driver.find_element_by_name('prize_open_type').send_keys('3')
            self.driver.find_element_by_name('prize_type').find_element_by_xpath("*//[@value=1]")
            self.driver.find_element_by_name('prize_count').send_keys('2')
            self.driver.find_element_by_name('share_img_url').send_keys('1')
            self.driver.find_element_by_class_name('btn_orange').click()
            logger.info('添加成功')
        except ZeroDivisionError as e:
            logger.warning('添加失败')
            return e

    def login(self, username, psw):
        logger.info('调用登录')
        self.driver.find_element_by_name("name").send_keys(username)
        self.driver.find_element_by_name("pwd").send_keys(psw)
        self.driver.find_element_by_name("code").send_keys("999999")
        self.driver.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(10)


if __name__ == "__main__":
    unittest.main()


