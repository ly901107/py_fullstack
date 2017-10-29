#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/28

# egg_list = []
#
# for i in range(100):
# 	egg_list.append('egg%s'% i)
# print(egg_list)
# egg_list = ['egg%s'%i for i in range(100)]
# print(egg_list)

#三元表达式
# name = 'alex'
# name = 'egon'
#
# res = 'sb' if name =='alex' else 'shuai'
# print(res)

# egg_list = ['egg%s'%i for i in range(100) if i >50]
# print(egg_list)

# l = [1,2,3,4,5]
# s = 'hello'
#
# l1= []

# import os

# def search():
# 	g = os.walk('C:\\egon')
# 	for i in g:
# 		for j in i[-1]:
# 			print('%s\\%s'%(i[0],j))
#
# search()
#
# import os
#
# g = os.walk('C:\\egon')
# l = ['%s\\%s'% (i[0],j) for i in g for j in i[-1]]
# print(l)

# egg_list = ('egg%s'%i for i in range(100))
# # print(egg_list)
# print(next(egg_list))

f = open('a.txt')
l1= (line.strip() for line in f)
print(next(l1))