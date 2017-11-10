#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/30

#编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录

import time
login_status = {'name':None,'login_time':0,'out_time':3}

def auth(auth_type):
	def auth1(func):
		def auth2(*args,**kwargs):
			timeout = time.time()-float(login_status['login_time'] )
			if timeout < login_status['out_time']:
				if login_status['name']:
					print('已登录，无需重复登录')
					res = func(*args,**kwargs)
					return res
			else:
				if auth_type == 'vip':
					with open('题目4_passwd',encoding='utf-8') as f:
						dic = eval(f.read())
					name = input('请输入VIP账号: ').strip()
					passwd= input('请输入VIP密码: ').strip()
					if name in dic and passwd == dic[name]:
						print('账号密码正确，进入VIP模块')
						res = func(*args, **kwargs)
						login_status['name'] = name
						login_status['login_time'] = time.time()
						return res
				else:
					print('进入普通模块')
					res = func(*args, **kwargs)
					login_status['login_time'] = time.time()
					return res
		return auth2
	return auth1


@auth(auth_type='general')
def foo1():
	print('from foo1')

@auth(auth_type='vip')
def foo2():
	print('from foo2')

@auth(auth_type='vip')
def foo3():
	print('from foo3')


foo3()
foo3()
time.sleep(5)
foo3()
time.sleep(2)
foo3()
foo1()