from selenium import webdriver
from common.Excel import ExcelUtil
import ddt
import unittest
import time

filePath = "F:\\test_demo\\Excel\\Excel.xlsx"
sheetName = "Sheet1"
test_data = ExcelUtil(filePath, sheetName).dict_data()
print(test_data)

#testdata = [{"username":"admin","psw":"123456"}]

@ddt.ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUp(cls):
        print('-------测试开始--------')
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://192.168.106.211:8100/")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDown(cls):
        print('-------测试结束--------')
        pass

    @ddt.data(*test_data)
    def test_login_01(self, data):
        print('-----数据加载，获取登录账号-----')
        print("测试数据：%s" % data)
        # 调用登录方法
        self.login(data['username'], data['psw'])
        time.sleep(10)

    def login(self, username, psw):
        print('-----登录-----')
        try:
            self.driver.find_element_by_name("name").send_keys(username)
            self.driver.find_element_by_name("pwd").send_keys(psw)
            self.driver.find_element_by_name("code").send_keys("999999")
            self.driver.find_element_by_xpath("//*[@type='submit']").click()
            time.sleep(5)
            print('------登录成功-------')
        except:
            print('-----登录失败--------')


if __name__ == "__main__":
    unittest.main()


