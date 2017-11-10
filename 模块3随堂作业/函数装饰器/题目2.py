#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/30

#编写装饰器，为函数加上统计时间的功能

import time

def init(func):
	def foo(*args,**kwargs):
		start_time=time.time()
		res=func(*args,**kwargs)
		stop_time=time.time()
		print('run time is %s'%(stop_time - start_time))
		return res
	return foo


@init
def statistics():
	print('开始运行程序')

statistics()