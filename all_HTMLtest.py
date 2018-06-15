'''
__data__ = 2017/11/16
__author__ = amy liu
'''

# coding = utf-8

import unittest
import time
from HTMLTestRunner import HTMLTestRunner

# 定义测试用例的目录为当前目录
test_dir = './test_case'


def all_case():
    # test case 所放的位置在 test_case 下面类型文件名为 test***.py 的文件
    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern='test*.py'
                                                   )
    print(u'读取测试用例：' + str(discover))
    return discover


# 获取当前系统时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# 测试报告命名
filename = '.\\report\\' + now + '.html'
# 测试报告存放路径
report_path = open(filename, 'wb')

runner = HTMLTestRunner(
    stream=report_path,
    title=u'自动化测试报告，测试结果如下：',
    description=u'测试用例执行情况：')

if __name__ == "__main__":
    # 执行测试用例
    runner.run(all_case())
    report_path.close()
