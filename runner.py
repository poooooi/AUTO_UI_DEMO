import os
import unittest
import time
from utils.HTMLTestRunner import HTMLTestRunner
from utils.utilConfig import CASE_PATH, REPORT_PATH

"""
执行用例并发送报告，分四个步骤:
第一步：加载用例
第二步：执行用例
第三步：获取最新的测试报告
第四步：发送邮件
"""
 
 
# log = logger(logger='run').getlog()


def add_case(caseName = 'case', rule='test*.py'):
    # 第一步：加载所有测试用例
    case_path = os.path.join(CASE_PATH, caseName)

    if not os.path.exists(case_path):
        os.mkdir(case_path)

    # 定义discover方法的参数(执行全部用例)
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    return discover


def run_case(all_case, reportName = 'report'):
    # 第二步：执行所有的用例，并把执行结果写入HTML测试报告中

    now = time.strftime('%Y%m%d_%H%M%S_', time.localtime(time.time()))

    if not os.path.exists(REPORT_PATH):
        os.mkdir(REPORT_PATH)

    report_abspath = os.path.join(REPORT_PATH, now + reportName + '.html')

    with open(report_abspath, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp, title='web自动化测试报告', description='用例执行情况')
        runner.run(all_case)


if __name__ == '__main__':
    # 第一步：加载用例
    cases = add_case()
    # 第二步：执行用例并生成HTML报告
    run_case(cases)
