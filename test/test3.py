#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/15

#函数形参、实参、万能参
#*args **kwargs
# if a > b:
#     c = y
# else:
#     c = x

# a = ['a','b']
# d = a
# 深浅拷贝

#环境变量
#sys.path 环境变量列表

#1*2+3*4+5*6+7*8...+99*100

# total = 0
# j = 0
# for i in range(1,101,2):
#     j = i + 1
#     total = total + i * j
#     # print(i,j)
# # eval()
# print(total)

# l2 = ["alex", 123, 'eric']
# a = [i for i in range(101)]
# print(a)

#装饰器原理

# def foo(func):
#     def foo1(*args,**kwargs):
#         print('before')
#         res = func(*args,**kwargs)
#         print('after')
#         return res
#     return foo1
#
#
#
# @foo
# def f1(arg):
#     return arg + 1
#
# @foo
# def f2(arg1, arg2):
#     return arg1 + arg2
#
# print(f1(1))
# print(f2(1,2))

# def outer(func):
#     def inner():
#         ...
#     return inner()
#
# @outer()
# def f1(arg):
#     ...

#迭代器 可迭代对象 生成器
#存储数据的数据结构

#六位的随机验证码(字符串)

# import string 模块

# while True:
#     s = input('Enter something: ')
#     if s == 'quit':
#         break
#     print('lenght of the string is', len(s))
# print('Done')


num = int(0.1)
print(num)