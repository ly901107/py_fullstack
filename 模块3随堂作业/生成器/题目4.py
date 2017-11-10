#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/31

#实现功能: grep -rl 'python' C:\egon


import os

def init(func):
	def foo(*args,**kwargs):
		res = func(*args,**kwargs)
		next(res)
		return res
	return foo

@init
def searcher(target):
	'查找路径'
	while True:
		dir_path = yield
		g=os.walk(dir_path)
		for i in g:
			for j in i[-1]:
				file_path = '%s\\%s'%(i[0],j)
				target.send(file_path)

@init
def opener(target):
	'打开文件，获取文件句柄'
	while True:
		file_path = yield
		with open(file_path,encoding='utf-8') as f_read:
			target.send((f_read, file_path))

@init
def reader(target):
	'读取文件'
	while True:
		f_read,file_path = yield
		for line in f_read:
			target.send((line, file_path))

@init
def greper(target,keyword):
	'过滤文件'
	while True:
		line,file_path = yield
		if keyword in line:
			target.send(file_path)

@init
def printer():
	'打印路径'
	while True:
		file_path = yield
		print(file_path)

g=searcher(opener(reader(greper(printer(),'python'))))
# g1=searcher()
# next(g)
g.send('C:\\egon')
