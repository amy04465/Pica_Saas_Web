'''
__data__ = 2017/11/16
__author__ = amy liu
'''

# coding = utf-8
from imp import reload
import os

import unittest
import time
import HTMLTestRunner

# 用例路径
# test_dir = './test_case'

# 加载用例
def add_case(case_path, rule):
    testunit = unittest.TestSuite()
    # test case 所放的位置在 test_case 下面类型文件名为 test***.py 的文件
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule
                                                   )
    testunit.addTests(discover)
    print(u'读取测试用例：' + str(discover))
    return discover

def run_case(all_case, report_path):
    '''执行所有的用例, 并把结果写入测试报告'''
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # 测试报告命名
    # filename = './report/' + now + '.html'
    report_abspath = os.path.join(report_path, now+".html")
    # 测试报告存放路径
    report_path = open(report_abspath, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=report_path,
        title=u'自动化测试报告，测试结果如下：',
        description=u'测试用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case)
    report_path.close()


if __name__ == "__main__":
    # 测试用例的路径、匹配规则
    rule = "test*.py"
    case_path =  './test_case'
    all_case = add_case(case_path, rule)   # 1加载用例
    # 生成测试报告的路径
    report_path = './report'
    run_case(all_case, report_path)        # 2执行用例
