#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/15

# #多态:同一种事物的多种形态，动物分为人类、猪类
# class Animal:
#     def run(self):
#         raise AttributeError('子类必须实现这个方法')
#
# class People(Animal):
#     def run(self):
#         print('人在跑')
#
# class Pig(Animal):
#     def run(self):
#         print('猪在跑')
#
# peo1 = People()
# pig1 = Pig()
#
# # peo1.run()
# # pig1.run()
#
# #多态性依赖于:
#     # 1.继承
#     # 2.
# #多态性:定义统一的接口
# def fun(obj):       #obj这个参数没有类型限制,可以传入不同类型的值
#     obj.run()       #调用的逻辑一样,执行的结果却不一样
#
# fun(peo1)
# fun(pig1)

class A:
    __x =1      #_A__x = 1
    def __test(self):
        print('from A')
        print(self)


a = A()

# print(A.__dict__)       #_A__x': 1
# print(A._A__x)          #1
# print(a._A__x)          #1

A._A__test(A)           #from A
# a._A__test()            #from A


#注意：__名字,这种语法，只在定义的时候才会有变形的效果,如果类或者对象已经产生了,就不会有变形效果

# class B:
#     pass
#
# B.__x = 1
#
# print(B.__x)            #1
# print(B.__dict__)       #'__x': 1
#
# b = B()
# b.__x = 1
# print(b.__x)            #1
# print(b.__dict__)       #'__x': 1

# class A:
#     def __init__(self):
#         self.__x = 1
#
#     def tell(self):
#         print(self.__x)
#
# a = A()
# a.tell()

# #在定义阶段就会变形
# class A:
#     def __fa(self):     #_A__fa
#         print('from A')
#
#     def test(self):
#         self.__fa()     #self._A__fa
#
# class B(A):
#     def __fa(self):     #_B__fa
#         print('from B')
#
# b = B()
# b.test()        #from A


# class Student(object):
#
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#     def get_name(self):
#         return self.__name
#
# bart = Student('Bart Simpson', 98)
# print(bart.get_name())
# bart.__name = 'New Name'
# print(bart.get_name())
# print(bart.__name)
# print(bart.__dict__)