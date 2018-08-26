from selenium import webdriver
from common.Excel import ExcelUtil
import ddt
import unittest
import time

filePath = "E:\\app_demo\\Excel\\test.xlsx"
sheetName = "Sheet1"
test_data = ExcelUtil(filePath, sheetName).dict_data()

# testdata = [{"username":"admin","psw":"123456"}]

@ddt.ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        print(cls.driver)
        cls.driver.get("http://www.baidu.com/")
        cls.driver.maximize_window()
        data = cls.driver.title
        print(data)
        cls.driver.find_element_by_link_text("登录").click()
        time.sleep(10)
        cls.driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_3__footerULoginBtn']").click()


    def login(self, username, psw):
        self.driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_3__userName']").send_keys(username)
        self.driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_3__password']").send_keys(psw)
        self.driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_3__submit']").click()
        time.sleep(10)

    @ddt.data(*test_data)
    def test_login(self, data):
        print("测试数据%s" % data)
        # 调用登录方法
        self.login(data['username'], data['psw'])
    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()
    print("huituibanben")


