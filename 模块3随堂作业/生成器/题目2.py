#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/31

#模拟管道，实现功能:tail -f access.log | grep '404'

import time

def my_tail(file_path):
	with open(file_path) as f:
		f.seek(0,2)
		while True:
			line = f.readline()
			if not line:
				time.sleep(1)
				continue
			else:
				yield line

def my_grep(keyword,lines):
		for line in lines:
			if keyword in line:
				yield line

g=my_tail('test')
g1=my_grep('404',g)

for i in g1:
	print(i)


