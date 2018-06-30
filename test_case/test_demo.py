'''
__data__ = 2017/11/24
__author__ = amy liu
'''


# 对于普通方法
# 当实例调用时，默认将当前实例传进去
# 类调用时，只能以 类名.method(类实例) 形式调用
class DemoClass1:
    def classPrint(self):
        print("class method")

    def objPrint(self):
        print("obj method")

# 必须实例化
obj = DemoClass1()

# 通过 类 来调用函数
DemoClass1.classPrint(obj)
DemoClass1.objPrint(obj)

# 通过 实例 来调用函数
obj.classPrint()
obj.objPrint()

# 对于classmethod方法
# 当实例调用classmethod方法时，默认会把当前实例所对应的类传进去
# 当类调用classmethod方法时，默认把此类传进去
class DemoClass2:
    @classmethod
    def classPrint(self):
        print("class method")

    def objPrint(self):
        print("obj method")


# 当实例调用classmethod方法时，默认会把当前实例所对应的类传进去
# 不需要实例化，不需要加self
DemoClass2.classPrint()
# 当类调用classmethod方法时，默认把此类传进去
obj = DemoClass2()
obj.classPrint()


# 对于staticmethod方法
# 实例和类调用，没有默认的参数传进函数
class DemoClass3:
    @staticmethod
    # 不需要传入参数
    def classPrint():
        print("class method")

    def objPrint(self):
        print("obj method")


DemoClass3.classPrint()

