#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/20

# class Foo:
#     country = 'China'
#
#     def __init__(self,name):
#         self.name = name
#
#     def walk(self):
#         print('%s is walking'%self.name)
#
# p = Foo('lex')
# res = getattr(p,'country')        #res = p.country
# print(res)                        #China
#
# f = getattr(p,'walk')             #w = p.walk
# print(f)                          #<bound method Foo.walk of <__main__.Foo object at 0x000000000217B2E8>>
#
# f1 = getattr(Foo,'walk')          #f1 = Foo.walk
# print(f1)                         #<function Foo.walk at 0x0000000001EAAA60>
#
# #注意:
# f()                               #即可运行 = p.walk()          lex is walking
# f1(p)                             #需将对象传入 = Foo.walk(p)    lex is walking
# print(getattr(p,'xxxxxx','这个不存在'))      #这个不存在
#
# # print(hasattr(p,'name'))        #True
# # print(hasattr(p,'country'))     #True      p.country
# # print(hasattr(Foo,'country'))   #True      Foo.country
#
# # setattr(p,'age',18)               #p.age = 18
# # print(p.__dict__)                 #{'name': 'lex', 'age': 18}
#
# print(p.__dict__)                   #{'name': 'lex'}
# delattr(p,'name')                   #del p.name
# print(p.__dict__)                   #{}

# class Foo(object):
#     staticField = "old boy"
#
#     def __init__(self):
#         self.name = 'wupeiqi'
#
#     def func(self):
#         return 'func'
#
#     @staticmethod
#     def bar():
#         return 'bar'
#
#
# print(getattr(Foo, 'staticField'))
#
# print(getattr(Foo, 'func'))
#
# print(getattr(Foo, 'bar'))

# class BlackMedium:
#     feature='Ugly'
#     def __init__(self,name,addr):
#         self.name=name
#         self.addr=addr
#
#     def sell_house(self):
#         print('%s 黑中介卖房子啦,傻逼才买呢,但是谁能证明自己不傻逼' %self.name)
#     def rent_house(self):
#         print('%s 黑中介租房子啦,傻逼才租呢' %self.name)
#
# b1=BlackMedium('万成置地','回龙观天露园')
#
# setattr(b1,'sb',True)
# setattr(b1,'show_name',lambda self:self.name+'sb')
# print(b1.__dict__)
# print(b1.show_name(b1))


# class Foo(object):
#     staticField = "old boy"
#
#     def __init__(self):
#         self.name = 'wupeiqi'
#
#     def func(self):
#         return 'func'
#
#     @staticmethod
#     def bar():
#         return 'bar'
#
# f = Foo()
#
# print(getattr(Foo, 'staticField'))
#
# print(getattr(Foo, 'func')(f))
#
# print(getattr(Foo, 'bar')())

# import sys
#
# class Foo:
#
#     def s1(self):
#         print('s1')
#
#
#     def s2(self):
#         print('s1')
#
#
# this_module = sys.modules[__name__]
#
# res = hasattr(this_module, 's1')
# print(res)
# # getattr(this_module, 's2')

# import importlib
#
# t = importlib.import_module('time')
# print(t.time())