#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/31

#编写日志装饰器，实现功能如：一旦函数f1执行，
# 则将消息2017-07-21 11:12:11 f1 run写入到日志文件中，日志文件路径可以指定
# 注意：时间格式的获取
# import time
# s=time.strftime('%Y-%m-%d %X')

import time

def logger(logfile):
	def foo(func):
		def foo2(*args,**kwargs):
			with open(logfile,'a+',encoding='utf-8') as f:
				#需理解func.__name__
				f.write('%s %s run\n'%(time.strftime('%Y-%m-%d %X'), func.__name__))
			res=func(*args,**kwargs)
			return res
		return foo2
	return foo


@logger(logfile='a.txt')
def f1():
	print('from f1')
f1()