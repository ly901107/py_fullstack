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

flag_login = False		#判断是否登陆
flag_regular = False		#判断是否是老用户
import sys
import os

while True:
	username = input('Please input your username: ').strip()		#输入账号
	with open('shopping_regular','r',encoding='utf8') as f_regular:		#判断账户是否曾经购买过商品
		for line in f_regular:
			if username in line.strip():		#判断是否为老用户
				flag_regular = True
				break
	passwd = input('Please input your passwd: ').strip()		#输入密码
	with open('shopping_user','r',encoding='utf8') as f_user:
		for line in f_user:		#验证账号密码
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
		print('以前购买商品如下'.center(25, '-'))
		print('名称          数量          单价')
		with open('shopping_history','r',encoding='utf8') as f_history:
			for line in f_history:
				if username in line.strip():
					f_history_str = str(line)
					f_history_dict = eval(f_history_str)
					for key,values in f_history_dict[username].items():		#遍历购物记录并打印
						print('%s%10s%10s'%(key,values[0],values[1]))
		print('End'.center(25, '-'))
	total_cost = 0		#购物总花费
	shopping_cart = {}		#购物车
	shopping_cart_history = {}		#购物车历史信息
	shopping_list = [
		["iphone7", 5800],
		["臭豆腐", 100],
		["甜不辣", 20],
		["拖鞋", 50],
		["coffee", 200]
	]		#购物清单
	while True:		#购物循环
		num = 1		#商品序号
		print('商品信息'.center(20, '-'))
		for key in shopping_list:		#打印出商品列表
			print(num, key)
			num += 1
		choice = input("请输入商品编号或'q'退出: ").strip()		#输入商品编号
		if choice == 'q':		#输入为q
			print('购买商品如下'.center(25,'-'))
			print('ID   名称          数量          单价')
			id_num = 1
			for key in shopping_cart:		#打印出购物信息
				msg = ("%d%10s%10s%15s"%
					   (id_num, key, shopping_cart[key][0],shopping_cart[key][1]))
				print(msg)
				id_num += 1
				total_cost += int(shopping_cart[key][0]) * int(shopping_cart[key][1])		#打印总花费及余额
			if shopping_cart:		#购物车不为空，存储历史购物信息
				shopping_cart_history[username] = shopping_cart
				with open('shopping_history', 'w', encoding='utf8') as f_history_write:		#记录历史购物信息
						f_history_write.write(str(shopping_cart_history)+'\n')
			if not flag_regular:  # 不是老顾客，记录为老顾客
				with open('shopping_regular','a+',encoding='utf8') as f_regular_write:		#记录老顾客信息
					f_regular_write.write(username+'\n')
			print('共计消费%d元，余额为%s'%(total_cost,cash))
			print('End'.center(25,'-'))
			sys.exit()
		quantity = input('请输入要购买的数量: ').strip()  # 输入购买数量
		if choice.isdigit() and quantity.isdigit():		#编号和数量是否只由数字组成
			choice = int(choice)
			quantity = int(quantity)
			if choice >0 and choice <= len(shopping_list):		#编号是否在范围内
				product = shopping_list[choice - 1]  # 商品列表为		product
				product_name = product[0]  # 商品名为		product[0]
				product_price = product[1]  # 商品价格为		product[1]
				cost = product_price * quantity			#单次购买花费为	cost
				if cost <= cash:		#判断是否买得起
					cash -= cost		#购买扣钱
					print('已购买商品%s，花费金额%s,账户余额为%s'%(product_name,cost,cash))
					if product_name in shopping_cart:		#商品名已存在购物车
						shopping_cart[product_name][0] += quantity
					else:		#商品第一次购买
						shopping_cart[product_name] = [quantity, product_price]		#将购买信息加入购物车
				else:
					print('账户余额不足，还差%s元'%(cost - cash))
					recharge = input('余额不足，是否进行充值 y/n: ').strip()		#询问是否充值
					if recharge == 'y':
						money = input('输入充值金额: ').strip()		#输入充值金额
						if money.isdigit():
							money = int(money)
							cash += money		#进行充值
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

		with open('shopping_user', 'r', encoding='utf8') as f_user_read,\
				open('shopping_user_recharge', mode='w', encoding='utf8') as f_user_write:	#实时保存账户余额
			for line in f_user_read:
				if username in line:
					line = ' '.join([username, passwd, str(cash) + '\n'])
				f_user_write.write(line)
		if os.path.isfile('shopping_user_bak'):  # 判断备份文件是否存在
			os.remove('shopping_user_bak')
		os.rename('shopping_user', 'shopping_user_bak')
		os.rename('shopping_user_recharge', 'shopping_user')
