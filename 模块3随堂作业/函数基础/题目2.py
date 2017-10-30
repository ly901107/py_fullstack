#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/30

#写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数

def check_str(msg):
	res = {
		'num':0,
		'string':0,
		'space':0,
		'other':0
	}
	for i in msg:
		if i.isdigit():		#判断是否是数字
			res['num'] += 1
		elif i.isspace():	#判断是否是空格
			res['space'] += 1
		elif i.isalpha():	#判断是否是字母
			res['string'] += 1
		else:	#字母串为other
			res['other'] += 1
	return res
res = check_str('1a -2b =3c +')
print(res)