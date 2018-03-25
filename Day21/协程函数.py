#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/28

# def foo(func):
# 	def foo1(*args,**kwargs):
# 		res = func(*args,**kwargs)
# 		next(res)
# 		return res		#此处理解 生成器是一次性的
# 	return foo1
#
# @foo		#eater = foo(eater) = foo1
# def eater(name):
# 	print('%s start to eat food '% name)
# 	food_list = []
# 	while True:
# 		food = yield food_list
# 		print('%s get %s, to start eat '% (name, food))
# 		food_list.append(food)
# 	print('Done')
#
# e = eater('钢蛋')		#foo1('钢蛋')
# # print(e.send('123'))
#
# print(type(e))

def eater(name):
    print('%s start to eat food '% name)
    food_list = []
    while True:
        food = yield food_list
        print('%s get %s, to start eat '% (name, food))
        food_list.append(food)
    print('Done')

e = eater('钢蛋')

print(next(e))
print(e.send('包子'))
print(e.send('韭菜包子'))    #send 等同于next 有返回值，但是会把后面的参数传给当前行的yield
print(e.send('馅饼'))