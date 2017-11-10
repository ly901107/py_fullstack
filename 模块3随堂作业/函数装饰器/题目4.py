#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/30

#编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
#注意：从文件中读出字符串形式的字典，可以用eval('{"name":"egon","password":"123"}')转成字典格式

login_status={'name':None,'passwd':None}

def auth(auth_type):
	def auth1(func):
		'认证函数'
		def auth2(*args,**kwargs):
			#账号已登录
			if login_status['name'] and login_status['passwd']:		#已登录的思路
				print('have login')
				res = func(*args,**kwargs)
				return res			#此处需理解
			if auth_type == 'vip':
				#账号没有登录
				with open('题目4_passwd', 'r', encoding='utf-8') as f:
					dic=eval(f.read())			#文件读取 需加强
				print(dic)
				name = input('input your name: ').strip()
				passwd = input('input your passwd: ').strip()
				if name in dic and passwd == dic[name]:
					login_status['name'] = name
					login_status['passwd'] = passwd
					print('VIP login success')
					res=func(*args,**kwargs)
					return res
				else:
					print('input error')
			else:
				print('还没想好')
		return auth2
	return auth1


@auth
def foo1():
	'foo1'
	print('welcome to foo1')

@auth(auth_type = 'vip')
def foo2():
	'函数home'
	print('welcome to foo2')

# @auth1(auth_type = 'vip')
@auth(auth_type = 'vip')
def foo3():
	'特殊模块'
	print('1024你懂得')

# foo1()
foo2()
foo2()
foo2()