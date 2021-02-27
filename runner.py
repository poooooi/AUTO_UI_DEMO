import os
import unittest
import time
from utils.HTMLTestRunner import HTMLTestRunner
from utils.emails import Email
from utils.utilConfig import CASE_PATH, REPORT_PATH

"""
执行用例并发送报告，分四个步骤:
第一步：加载用例
第二步：执行用例
第三步：获取最新的测试报告
第四步：发送邮件
"""

def add_case(rule='test*.py'):
    # 第一步：加载所有测试用例
    if not os.path.exists(CASE_PATH):
        os.mkdir(CASE_PATH)

    # 定义discover方法的参数(执行全部用例)
    discover = unittest.defaultTestLoader.discover(CASE_PATH, pattern=rule, top_level_dir=None)
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

def get_report_file(REPORT_PATH):
    # 第三步：获取最新的测试报告
    lists = os.listdir(REPORT_PATH)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(REPORT_PATH, fn)))

    print('最新测试报告：' + lists[-1])

    # 找到最新的测试报告文件
    report_file = os.path.join(REPORT_PATH, lists[-1])
    return report_file


if __name__ == '__main__':
    # 第一步：加载用例
    cases = add_case()
    # 第二步：执行用例并生成HTML报告
    run_case(cases)
    # 第三步：获取最新的测试报告
    report_file = get_report_file(REPORT_PATH)
    # 第四步：发送邮件
    Email(title='百度搜素测试报告',
          message='这是今天的测试报告，请查收！',
          receiver='收件方邮箱',
          server='smtp.qq.com',
          sender='发送方邮箱',
          password='发送方鉴权码',
          path=report_file
          ).send()