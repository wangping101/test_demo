import os
import unittest
import STHTMLTestRunner
# 用例路径
# case_path = os.path.join(os.getcwd(), "appium_demo")
# 报告存放路径
# report_path = "E:\\app_demo\\report"
case_path = os.path.abspath("..\\interface")


def all_case():
    runner1 = unittest.defaultTestLoader.discover(case_path,
                                                  pattern="test_05.py",
                                                  top_level_dir=None)
    return runner1


if __name__ == "__main__":
    # unittest.main()
    report_path = os.path.join("..\\report", "report.html")
    fp = open(report_path, "wb")
    runner = STHTMLTestRunner.HTMLTestRunner(stream=fp,
                                             title=U'自动化测试报告',
                                             description=u'用例执行情况：')
    # runner = unittest.TextTestRunner()
    runner.run(all_case())
    fp.close()














































