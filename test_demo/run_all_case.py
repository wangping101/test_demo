import os
import unittest
from common.Logger import Log
# import HTMLTestRunner  # 仅提供html文字报告
import STHTMLTestRunner  # 可提供带html的饼图及截图报告

# 用例路径
case_path = os.path.join(".\\selenium_xuexi")


def all_case():
    case = unittest.defaultTestLoader.discover(case_path,
                                               pattern='test_*.py',
                                               top_level_dir=None)
    print(case)
    return case


if __name__ == "__main__":
    # 报告存放路径
    report_path = os.path.join(".\\report\\report.html")
    fp = open(report_path, "wb")
    runner = STHTMLTestRunner.HTMLTestRunner(stream=fp,
                                             title=U'自动化测试报告',
                                             description=u'用例执行情况：')
    runner.run(all_case())
    fp.close()
