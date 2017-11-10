#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/31

#求文件a.txt中总共包含的字符个数？思考为何在第一次之后的n次sum求和得到的结果为0？（需要使用sum函数）

with open('a.txt',encoding='utf-8') as f:
	print(sum(len(line) for line in f))
	print(sum(len(line) for line in f))
	print(sum(len(line) for line in f))
