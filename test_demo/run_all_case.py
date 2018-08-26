import os
import unittest
# import HTMLTestRunner  # 仅提供html文字报告
import STHTMLTestRunner  # 可提供带html的饼图及截图报告


# 用例路径
case_path = os.path.join("E:\\", "app_demo", "selenium_xuexi")


def all_case():
    runner1 = unittest.defaultTestLoader.discover(case_path,
                                                  pattern='test*.py',
                                                  top_level_dir=None)
    print(runner1)
    return runner1


if __name__ == "__main__":
    # 报告存放路径
    report_path = os.path.join("E:\\app_demo\\report", "report.html")
    fp = open(report_path, "wb")
    runner2 = STHTMLTestRunner.HTMLTestRunner(stream=fp,
                                              title=U'自动化测试报告',
                                              description=u'用例执行情况：')
    # runner2 = unittest.TextTestRunner()
    runner2.run(all_case())
    fp.close()













