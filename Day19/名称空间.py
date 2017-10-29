#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/25


def f1():
	x = 1
	print('----->f1 ',x)
	def f2():
		x = 2
		print('---->f2 ',x)
		def f3():
			x = 3
			print('--->f3 ',x)
		f3()
	f2()
f1()

