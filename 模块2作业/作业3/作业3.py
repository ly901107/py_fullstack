#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/14

# 购物车
#     1. 商品信息- 数量、单价、名称		商品信息通过列表的相互嵌套实现
#     2. 用户信息- 帐号、密码、余额		将用户信息保存至文件shopping_user
#     3. 用户可充值		对shopping_user中的余额进行修改
#     4. 购物历史信息			退出时查看已购买商品
#     5. 允许用户多次购买，每次可购买多件
#     6. 余额不足时进行提醒
#     7. 用户退出时 ，输出当次购物信息			购物车shopping_cart 字典输出
#     8. 用户下次登陆时可查看购物历史			判断是否购买过shopping_regular
# 		 将用户此次购物信息存入到历史购物文件shopping_history
#     9. 商品列表分级显示			for循环打印

flag_login = False
flag_regular = False
import sys
import  os

while True:
	username = input('Please input your username: ').strip()		#输入账号密码
	with open('shopping_regular','r',encoding='utf8') as f_regular:		#判断账户是否曾经购买过商品
		for line in f_regular:
			if username in line.strip():
				flag_regular = 	True		#购买过flag_regular为True
				break

	passwd = input('Please input your passwd: ').strip()
	with open('shopping_user','r',encoding='utf8') as f_user:
		for line in f_user:
			f_username,f_passwd,balance = line.strip().split()
			if username == f_username and passwd == f_passwd:		#账号密码正确
				print('登陆成功,账户余额为%s'%balance)		#登陆并打印余额
				cash = int(balance)
				flag_login = True
				break
		if not flag_login:		#账户密码错误
			print('账号密码输入错误，请重新输入！')
			continue

	if flag_regular:		#判断为老顾客并打印购物记录
		print('=================老顾客')

	shopping_cart = {}		#购物车
	shopping_list = [
		["iphone7", 5800],
		["臭豆腐", 100],
		["甜不辣", 20],
		["拖鞋", 50],
		["coffee", 200]
	]
	while True:
		num = 1
		print('商品信息'.center(20, '-'))
		for key in shopping_list:		#打印出商品列表
			print(num, key)
			num += 1

		choice = input("请输入商品编号或'q'退出: ").strip()		#输入商品编号
		quantity = input('请输入要购买的数量: ').strip()		#输入购买数量
		if choice == 'q':
			print('==========打印购物车并退出')
		if choice.isdigit() and quantity.isdigit():		#字符串是否只由数字组成
			choice = int(choice)
			quantity = int(quantity)
			if choice >0 and choice < len(shopping_list):		#编号是否在范围内
				product = shopping_list[choice-1]		#商品列表为		product
				product_name = product[0]				#商品名为		product[0]
				product_price = product[1]				#商品价格为		product[1]
				cost = product_price * quantity			#单次购买花费为	cost
				if cost <= cash:		#判断是否买得起
					print('购买成功')
					sys.exit()
				else:
					print('账户余额不足，还差%s元'%(cost - cash))
					recharge = input('余额不足，是否进行充值 y/n: ').strip()		#询问是否充值
					if recharge == 'y':
						money = input('输入充值金额: ').strip()		#输入充值金额
						if money.isdigit():
							money = int(money)
							cash += money		#进行充值
							with open('shopping_user','r',encoding='utf8') as f_user_read,\
								open('shopping_user_recharge',mode='w',encoding='utf8') as f_user_write:
								for line in f_user_read:
									if username in line:
										line = ' '.join([username,passwd,str(cash)+'\n'])
									f_user_write.write(line)
							if os.path.isfile('shopping_user_bak'):		#判断备份文件是否存在
								os.remove('shopping_user_bak')
							os.rename('shopping_user','shopping_user_bak')
							os.rename('shopping_user_recharge','shopping_user')
							print('充值成功,余额为%s'%cash)
					elif recharge == 'n':
						continue
					else:
						print('输入错误，退出充值')
						continue
			else:
				print('输入错误，请重新输入！')
				continue
		else:
			print('输入错误，请重新输入！')
			continue
