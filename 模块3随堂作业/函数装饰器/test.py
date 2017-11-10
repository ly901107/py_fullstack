#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/31

# def outer():
#     x = 1
#     def inner():
#         print(x)
#     inner()
#
# outer() # 1

# def f1():
#     x = 1
#     print('----->f1 ',x)
#     def f2():
#         x = 2
#         print('---->f2 ',x)
#         def f3():
#             x = 3
#             print('--->f3 ',x)
#         f3()
#     f2()
# f1()

# route_dic={}
#
# def make_route(name):
#     def deco(func):
#         route_dic[name]=func
#     return deco
# @make_route('select')
# def func1():
#     print('select')
#
# @make_route('insert')
# def func2():
#     print('insert')
#
# @make_route('update')
# def func3():
#     print('update')
#
# @make_route('delete')
# def func4():
#     print('delete')
#
# print(route_dic)

# import time
# s=time.strftime('%Y-%m-%d %X')
# print(s)

def logged(func):
    def with_logging(*args, **kwargs):
        print (func.__name__)      # 输出 'with_logging'
        print (func.__doc__)       # 输出 None
        return func(*args, **kwargs)
    return with_logging

# 函数
@logged
def f(x):
   """does some math"""
   return x + x * x
print(f.__name__)
# f(1)