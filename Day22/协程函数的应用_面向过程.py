#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/28

# grep -rl 'python' C:\egon
import os

#装饰器，将生成器next初始化
def init(func):
	def foo(*args,**kwargs):
		res = func(*args,**kwargs)
		next(res)
		return res
	return foo

@init
def search(target):
	'查找文件绝对路径'
	while True:
		dir_path = yield		#此yield放在while外还是内有疑问:yield放在while外就会造成死循环，无法进行下次yield
		g = os.walk(dir_path)		#g为迭代器
		for i in g:
			# print(i)
			for j in i[-1]:
				file_path = '%s\\%s'%(i[0],j)
				target.send(file_path)

@init
def opener(target):
	'打开文件获取文件句柄'
	while True:
		file_path = yield
		with open(file_path) as f:
			target.send((f,file_path))

@init
def cat(target):
	'读取文件内容'
	while True:
		f,file_path = yield
		for line in f:		#读取一行文件
			target.send((line,file_path))

@init
def grep(target,pattern):	#传递两个参数，其中pattern为要过滤的字符串
	'过滤文件一行中是否有python'
	while True:
		line,file_path = yield
		if pattern in line:
			target.send(file_path)		#需传递文件路径

@init
def printer():
	'打印文件路径'
	while True:
		file_path = yield
		print(file_path)

g=search(opener(cat(grep(printer(),'python'))))
g.send('C:\\egon')