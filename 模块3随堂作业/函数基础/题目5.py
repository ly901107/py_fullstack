#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/30

#写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。

def func(msg):
	msg = msg[1::2]
	return msg

res = func([0,1,2,3,4,5,6])
print(res)
