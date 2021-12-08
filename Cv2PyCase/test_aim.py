#!/usr/bin/python3

class MyClass:
    """一个简单的类实例"""
    i = 'ma la xiang guo'
    j = 'ji dan chao fan'
    k = 'suan la tu dou si'

    def f(self):
        return 'hello world'

    def m(self):
        return "hello lua"

    def n(self):
        return "hello c++"

# 实例化类

x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.n())
print("MyClass 类的方法 f 输出为：", x.m())
print("MyClass 类的属性 f 输出为：", x.f)


