# class string():
#     l = [1,2,3,4,5]
#     def var(self):
#         for i in range(10):
#             print(i+1)
#
#     def arc(self):
#          print("abc")
#
# run = string()
# run.l = [12,23,45,56]
# print(run.l)
# run.var()
# run.arc()


# class demo():
#     __a = 0
#     def al(self):
#         self.__a = 1

# class Parent:  # 定义父类
#     def myMethod(self):
#         print('调用父类方法')
#
#
# class Child(Parent):  # 定义子类
#     def myMethod(self):
#         print('调用子类方法')
#
#
# c = Child()  # 子类实例
# c.myMethod()  # 子类调用重写方法
# super(Child,c).myMethod()  # 用子类对象调用父类已被覆盖的方法

# from module import say

# import calendar
# print(calendar.February)
# print(calendar.monthrange(2020,9))
#
# import requests

class tel_num():
    list = ["136","131"]
    def num(self):
        import random
        a = random.choice(self.list)
        print(a)


class Number():
    l = ["186","138", "139", "169", "123"]
    # l = ["186"]
    @classmethod
    def tele_Number(cls):
        import random
        cls.tele_Num = random.choices(__class__.l, k=1)
        cls.tele_BodyNum = random.choices("0123456789", k=8)
        print("".join(cls.tele_Num + cls.tele_BodyNum))
Number.tele_Number()
sd = Number()
sd.tele_Number()
print(sd.tele_Num)
# print(Number.tele_Number().tele_Num)
# Number.l.append("999")
# Number.tele_Number()


