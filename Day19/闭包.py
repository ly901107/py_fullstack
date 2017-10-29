#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/26

# x =1
#
# def f1():
# 	x = 1000
# 	def f2():
# 		print(x)
# 	return f2
#
# f = f1()
# f()
# print(f.__closure__[0])
# print(f.__closure__[0].cell_contents)

# from urllib.request import urlopen
# def get(url):
# 	return urlopen(url).read()
# # print(get('http://www.baidu.com'))
# print(get('http://www.python.org'))

# from urllib.request import urlopen
# def f1(url):
# 	def f2():
# 		print(urlopen(url).read())
# 	return f2
#
# baidu = f1('http://www.baidu.com')
# baidu()

x =1

def f1():
    x = 1000
    def f2():
        print(x)
    return f2

f = f1()
f()
print(f.__closure__[0])
print(f.__closure__[0].cell_contents)