#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/26

# def foo():
# 	print('foo')
# #
# # print(foo)
# #
# # f = foo
# # print(f)
#
# def bar(func):
# 	print(func)
# 	return func
#
# f = bar(foo)
# print(f)

#把函数当做容器类型的元素去用

def foo():
    print('foo')

def bar(func):
    # print(func)
    return func

f = bar(foo)
print(f)