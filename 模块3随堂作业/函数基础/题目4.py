#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/30

#写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者

def func(msg):
	if len(msg) > 2:
		msg = msg[:2]
	return msg

res = func([0,1,2,3,4,5])
print(func(res))
