#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/31

#自定义函数模拟range(1,7,2)

def my_range(start,stop,step=1):
	while start < stop:
		yield start
		start += step

g=my_range(1,7,2)
print(next(g))
print(next(g))
print(next(g))
# print(next(g))
