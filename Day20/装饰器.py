#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/26
# import time
# def timmer(func):
# 	def wrapper():
# 		start_time = time.time()
# 		func()
# 		stop_time = time.time()
# 		print('run time is %s ' % (stop_time - start_time))
# 	return wrapper
#
# @timmer		#index=timmer(index)
# def index():
# 	time.sleep(3)
# 	print('welcome to oldboy')
#
# index()		#wrapper()


# import  time
# def timmer(func):
# 	def foo(*args,**kwargs):
# 		start_time = time.time()
# 		func(*args,**kwargs)
# 		stop_time = time.time()
# 		print('run time is %s' % (stop_time - start_time))
# 	return foo
#
# @timmer
# def index(name):
# 	time.sleep(2)
# 	print('welconme to my home! %s' % name)
#
# @timmer
# def auth(name,passwd):
# 	print(name,passwd)
#
# index('egon')		#foo('egon')
# auth('liuyang','123')


# import time
# def timmer(func):
# 	def foo(*args,**kwargs):
# 		start_time = time.time()
# 		res = func(*args,**kwargs)
# 		stop_time = time.time()
# 		print('run time is %s '% (stop_time - start_time))
# 		return res
# 	return foo
#
# @timmer		# my_max = timmer(my_max)
# def my_max(x,y):
# 	res = x if x > y else y
# 	return res
#
# res = my_max(2, 3)		#foo(2, 3)
# print(res)

# def auth2(auth_type):
# 	def auth(func):
# 		def foo(*args,**kwargs):
# 			name = input('username: ').strip()
# 			passwd = input('passwd:')
# 			if auth_type == 'sql':
# 				if name == 'liuyang' and passwd == '123':
# 					print('auth successful')
# 					res = func(*args,**kwargs)
# 					return res
# 				else:
# 					print('auth error')
# 			else:
# 				print('还没学会')
# 		return foo
# 	return auth
#
# @auth2(auth_type = 'sql')
# def index():
# 	print('welcome to index page')
#
# index()


import time
from functools import wraps
def timmer(func):
    @wraps(func)
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('run time is %s ' % (stop_time - start_time))
    return wrapper

@timmer        #index=timmer(index)
def index():
    'come from index'
    print('welcome to oldboy')

index()        #wrapper()
print(index.__doc__)
