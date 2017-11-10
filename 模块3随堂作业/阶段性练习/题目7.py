#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/31

# 7 一个嵌套很多层的列表，如l=［1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]］，用递归取出所有的值

l=[1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]]

def get(target):
	for item in target:
		if type(item) is list:
			get(item)
		else:
			print(item)

get(l)