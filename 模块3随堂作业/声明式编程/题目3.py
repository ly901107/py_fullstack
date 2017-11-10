#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/31

#求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）

# with open('a.txt',encoding='utf-8') as f:
# 	for line in f:
# 		print(max(len(line)))

with open('a.txt',encoding='utf-8') as f:
	print(max(len(line) for line in f))

