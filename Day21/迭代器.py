#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/27


# b = {'a':1,'b':2,'c':3}
# i = iter(b)
# while True:
# 	try:
# 		print(next(i))
# 	except StopIteration:
# 		break
#
#
# for key in d:	#d即为d.__iter__ 迭代器放入原位置
# 	print(key)	#并且for循环具有异常捕捉的功能

# for i in b:
# 	print(i)

# from collections import Iterable,Iterator
#
# s = 'hello'
# l = [1,2,3]
# t = (1,2,3)
# d = {'a':1}
# set1 = (1,2,3,4)
# f = open('a.txt')

# s.__iter__()
# l.__iter__()
# t.__iter__()
# d.__iter__()
# set1.__iter__()
# f.__iter__()
# 									#Iterable 为可迭代的
# print(isinstance(s,Iterable))		#isinstance()  函数来判断一个对象是否是一个已知的类型，类似 type()。
# print(isinstance(l,Iterable))
# print(isinstance(t,Iterable))
# print(isinstance(d,Iterable))
# print(isinstance(set1,Iterable))
# print(isinstance(f,Iterable))

print(isinstance(s,Iterator))		#Iterator 为迭代器
print(isinstance(l,Iterator))
print(isinstance(t,Iterator))
print(isinstance(d,Iterator))
print(isinstance(set1,Iterator))
print(isinstance(f,Iterator))