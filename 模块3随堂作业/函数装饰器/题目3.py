#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/30

#编写装饰器，为函数加上认证的功能

def login(func):
	def foo(*args,**kwargs):
		name = input('input your name: ').strip()
		passwd = input('input your passwd: ').strip()
		if name == 'lex' and passwd == '123':
			print('login success')
			res=func(*args,**kwargs)
			return res
		else:
			print('your input error')
	return foo


@login
def start():
	print('进入主函数')

start()