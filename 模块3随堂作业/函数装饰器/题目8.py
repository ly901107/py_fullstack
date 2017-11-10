#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/30

#还记得我们用函数对象的概念，制作一个函数字典的操作吗，
# 来来来，我们有更高大上的做法，在文件开头声明一个空字典，然后在每个函数前加上装饰器，完成自动添加到字典的操作

route_dic={}

def make_route(name):
	def deco(func):
		route_dic[name] = func
	return deco
@make_route('select')		#func1=deco(func1)
def func1():
	print('select')

# @make_route('insert')
# def func2():
#     print('insert')
#
# @make_route('update')
# def func3():
#     print('update')
#
# @make_route('delete')
# def func4():
#     print('delete')
#
# print(route_dic)
print(route_dic)