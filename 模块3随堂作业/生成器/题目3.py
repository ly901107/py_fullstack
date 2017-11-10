#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/31

def init(func):
	def foo(*args,**kwargs):
		res=func(*args,**kwargs)
		next(res)
		return res
	return foo

@init
def eater(name):
    print('%s 准备开始吃饭啦' %name)
    food_list=[]
    while True:
        food=yield food_list
        print('%s 吃了 %s' % (name,food))
        food_list.append(food)

g=eater('egon')
g.send('大包子')
