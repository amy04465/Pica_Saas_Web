#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created on 2017/3/23 15:41
@author: Jason.ma

"""
import unittest
import json
from HTMLTestRunner import HTMLTestRunner


class exe(object):
    def __init__(self, exe_case):
        """
        装载要执行的测试用例套件
        :param exe_case: 测试用例模块
        data={"mod1":{"test_class1":["test_case1","test_case2"]},"mod2":{"test_class2":["test_case1","test_case2"]}}
        """
        self._test_class_suite = []
        self.suite = unittest.TestSuite()
        if type(exe_case) == dict:
            pass
        else:
            raise TypeError("请检查要执行的测试用例信息是否正确，应为dict类型")
        if len(exe_case):
            for (case_mod, tc_info) in exe_case.items():
                test_mod = __import__(case_mod)
                self.__add_suite(test_mod, tc_info)

    def execute_tc(self):
        unittest.TextTestRunner(verbosity=2).run(self.suite)

    def __add_suite(self, test_mod, tc_info):
        for (cls_name, tc_name) in tc_info.items():
            if hasattr(test_mod, cls_name):
                test_class_instance = getattr(test_mod, cls_name)
                for tc in tc_name:
                    self.suite.addTest(test_class_instance(tc))
            else:
                raise AttributeError(cls_name + "属性不存在")

# 1.需要执行的测试用例

# 2.需要执行的测试类

# 3.需要执行的测试模块
if __name__ == "__main__":

    pro_class = {"product": ["test_product_info", "test_product_rate", "test_product_verison"]}
    acc_class = {"account": ["test_account_amt", "test_account_name", "test_account_pwd"]}

    test_data = {"product": pro_class, "account": acc_class}
    test = exe(test_data)
    test.execute_tc()

# tc = {"product": "product", "account": "account"}
# suite = unittest.TestSuite()
# for (k, v) in data.items():
#     test_class = __import__(k)
#     for (i, j) in v.items():
#         test_instance = getattr(test_class, i)
#         for test in j:
#             suite.addTest(test_instance(test))
#
# unittest.TextTestRunner(verbosity=2).run(suite)

class exe_json_data(object):

    def __init__(self, json_data):

        pass

pro_class = {"product": ["test_product_info", "test_product_rate", "test_product_verison"]}
acc_class = {"account": ["test_account_amt", "test_account_name", "test_account_pwd"]}
test_data = {"product": pro_class, "account": acc_class}

jsons = json.dumps(test_data)
print (jsons)
# 解析json
data = json.loads(jsons)

print(data["product"]["product"])

