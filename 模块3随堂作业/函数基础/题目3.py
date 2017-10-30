#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/30

#写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
def check_len(msg):
	res = len(msg)
	if res > 5:
		print('length more than 5')
	else:
		print('length less than 6')

check_len([1,2,3,4,5,6])