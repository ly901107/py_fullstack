#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/30

#写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

dic = {"k1": "v1v1", "k2": [11,22,33,44]}

def func(msg):
	for k,v in msg.items():
		if len(v) >2:
			msg[k]=v[:2]
	return msg

res=func(dic)
print(res)