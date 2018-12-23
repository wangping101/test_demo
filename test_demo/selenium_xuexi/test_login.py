from selenium import webdriver
from common.Excel import ExcelUtil
from common.Oracle import OracleUtil
import ddt, os
import unittest
import time

try:
    # ---------------Excel封装调用取表中数据---------------------------
    filePath = os.path.join("..\\Excel\\test.xlsx")
    sheetName = "Sheet1"
    test_data = ExcelUtil(filePath, sheetName).dict_data()
    print(test_data)


except:
    # ---------------调用Oracle取数据库中取数据-------------------------
    oracl = OracleUtil()
    sql = "select t.user_name, t.psw  from th_user_info_ t where t.user_id is not null"
    s = oracl.oracle_getrows(sql)
    print(type(s))
    for i in s:
        s2 = ('username', 'psw', 'STATUS', 'CREATE_TIME', 'FANS_NAME')
        s3 = (dict(zip(s2, i)))
        test_data = []
        test_data.append(s3)
        print(test_data)


@ddt.ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        print(cls.driver)
        cls.driver.get("http://www.baidu.com/")
        cls.driver.maximize_window()
        cls.driver.find_element_by_link_text("登录").click()
        time.sleep(10)
        cls.driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_3__footerULoginBtn']").click()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

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


if __name__ == "__main__":
    unittest.main()
