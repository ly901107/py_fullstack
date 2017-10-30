#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/30

#写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作

import os
def modify_file(filename,old,new):
	with open(filename,'r',encoding='utf-8') as read_f, \
			open('F:\python_file_test\\a.bak','w',encoding='utf-8') as write_f:
		for line in read_f:
			if old in line:
				line=line.replace(old,new)
			write_f.write(line)
	os.remove(filename)		#os模块的应用
	os.rename('F:\python_file_test\\a.bak',filename)		#window 下 文件路径是\\

modify_file('F:\python_file_test\\test_modify_name.txt','alex','SB')