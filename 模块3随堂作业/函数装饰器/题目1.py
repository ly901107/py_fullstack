#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/30

#一：编写函数，（函数执行的时间是随机的）

import time,random

def init(func):
	def foo(*args,**kwargs):
		start_time = time.time()
		time.sleep(random.randint(1,5))
		res=func(*args,**kwargs)
		stop_time = time.time()
		print('sleep time is %s '% (stop_time - start_time ))
		return res
	return foo

@init
def start():
	print('开始执行函数')

start()