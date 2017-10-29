#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/27


# def test():
# 	print('one')
# 	yield 1
# 	print('two')
# 	yield 2
# 	print('three')
# 	yield 3
#
# g = test()		#无输出
# print(g)		#<generator object test at 0x00000000027E91A8>
# res = next(g)	#one
# print(res)		#1

# def countdown(n):
# 	print('start countdown')
# 	while n >0:
# 		yield n
# 		n -= 1
# 	print('done')
#
# g= countdown(5)

# print(next(g))		#start countdown	5
# print(next(g))		#4
# print(next(g))		#3
# print(next(g))		#2
# print(next(g))		#1
# print(next(g))		#done

# for i in g:
# 	print(i)
#
# while True:
# 	try:
# 		print(next(g))
# 	except	StopIteration:
# 		break

# def func():
# 	n = 0
# 	while True:
# 		yield n
# 		n += 1
#
# f = func()
# print(next(f))


# def tail(file_path):
# 	with open(file_path,'r') as f:
# 		f.seek(0,2)			#光标移到最后
# 		while True:
# 			line = f.readline()		#读这一行
# 			if not line:
# 				continue
# 			else:
# 				print(line)
def func():
    n=0
    while True:
        yield n
        n += 1
g=func()
res=next(g)
for i in g:
    print(i)
