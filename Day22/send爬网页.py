#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/28

# from urllib.request import urlopen

# def	foo1(url):
# 	def foo2():
# 		print(urlopen(url).read())
# 	return foo2
#
# baidu = foo1('http://www.baidu.com')
# baidu()


from urllib.request import urlopen

def my_next(func):
	def foo(*args,**kwargs):
		res = func(*args,**kwargs)
		next(res)
		return res
	return foo

@my_next
def get():

	while True:
		url = yield
		res = urlopen(url).read()		#爬网页返回值
		print(res)		#输出爬网页结果

g=get()
g.send('http://www.baidu.com')
# g.send('http://www.python.org')



