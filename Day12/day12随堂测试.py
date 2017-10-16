#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/9/29

#
# name = ["liudehua","yaoming","lialun"]
# # print(name)
# print(name[-3])

#作业1
#跳出多层循环 ，三层循环， 最里层，直接跳出3层， exit()
#for i in range

#写法1
flag = False
for i in range(10):		#第一层
	print("------i",i)
	if i > 5:
		for j in range(10):		#第二层
			print("======j",j)
			if j > 5:
				for k in range(10):		#第三层
					if k == 5:
						print("k", k)
						flag = True
				if flag is True:
					break
		if flag is True:
			break
	if flag is True:
		break

#写法2
def work():
	for i in range(10):  # 第一层
		print("------i", i)
		if i > 5:
			for j in range(10):  # 第二层
				print("======j", j)
				if j > 5:
					for k in range(10):  # 第三层
						if k == 5:
							print("k", k)
							return i,j,k
print(work())

#写法3
break_flag = True
count = 0
while break_flag:
	print("爷爷层。。。")
	while break_flag:
		print("爸爸层")
		while break_flag:
			print("孙子层")
			count += 1
			if count == 5:
				break_flag = False
#作业2
# 购物车程序
#     python shopping.py
#     input your salary: 5000
#     你可以买下面的东西：
#     1. iphone   5800
#     2. coffee   30
#     3. book  50
#     4. condom   90
#     >>: 1
#      买不起，打印差多少
#     >>:2
#     放入购物车，扣钱，同时打印余额。。。  4970
#     >>:3
#     ...
#     >>:4
#     >>:q
#     您买了下面的东西
#     coffee 30
#     book ..333
#     你还有多少前  3000
#     bye.
# 知识点
#       1 循环
#       2 列表