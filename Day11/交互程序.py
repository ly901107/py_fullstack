#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/9/28

# name = input ("input your name:")
# age = input ("input your age")
#
# print ( name , age )
#
# import getpass
#
# username = input("username")
# password = getpass.getpass("password")
#
# print(username, password)
#
# if username == "lex" and password == "123":
# 	print("welcome Lex!")
# else:
# # 	print("wrong username or password!")
# age = 50
#
#
# user_guess = int( input("input your guess") )
#
# if user_guess > age:
# 	print("try smaller...")
# elif user_guess< age:
# 	print("try bigger...")
# else:
# 	print("you get it!")

# for i in range(10):
# 	if i<5:
# 		continue #不往下走了 直接进入下一次loop
# 	print("loop:",i)

# count = 0
# while True:
# 	print("你是风儿我是沙，缠缠绵绵到天涯...",count)
# 	count += 1
# 	if count == 100:
# 		print("去你妈的风和沙，你们这些脱了裤子是人，穿上裤子是鬼的臭男人...")
# 		break

#作业1：实现让用户不断的猜年龄，但只给最多3次机会，再猜不对就退出程序
# age = 50
# count = 0
# while count < 3:
# 	user_guess = int(input("input your guess"))
# 	if user_guess > age:
# 		print("try smaller...")
# 		count += 1
# 	elif user_guess < age:
# 		print("try bigger...")
# 		count += 1
# 	else:
# 		print("you get it")
# 		break
# 	# if count == 3:
# 	# 	print("猜错三次，程序退出...")
# 	# 	break
# else:
# 	print("猜错三次，程序退出...")


#作业2：猜年龄，每隔3次问一下还想不想玩，y n
'''
age = 50
count = 0
while count < 3:
	user_guess = int(input("input your guess"))		#输入猜的年龄
	if user_guess > age:		#判断是否大于age
		print("try smaller...")
		count += 1
	elif user_guess < age:		#判断是否小于age
		print("try bigger...")
		count += 1
	else:
		print("you get it")
		break
	if count == 3:		#已经猜了3次
		user_play = input("play continue...y or n:")		#是否还想玩，输入 y 或者 n
		if 	user_play == "y":
			print("选择继续游戏")
			count = 0
		elif user_play == "n":
			print("选择退出游戏")
			break
'''

