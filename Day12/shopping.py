#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/9/30

# #输入工资
# #初始定义商品名及价格
# #输入想购买商品的编号
#
# salary = int( input("please input your salary:") )		#输入工资
# price_list = [3800, 30, 50, 90]		#列表-商品价格
# name_list = ["iphone", "coffee", "book", "condom"]		#列表-商品名字
# print("你可以买以下商品：\n",		#打印出商品组合
# "1.",name_list[0],price_list[0],"\n",
# "2.",name_list[1],price_list[1],"\n",
# "3.",name_list[2],price_list[2],"\n",
# "4.",name_list[3],price_list[3])
# total_list = []
#
# #判断工资是否足够购买商品
# while True:
# 	buy_num_input = input("please input the commodity number or 'q' to quit:")		#输入购买的或者退出
# 	if buy_num_input == "q":		#判断输入退出
# 		print("退出购买")
# 		print("已购买",name_list[0],total_list.count(name_list[0]))
# 		print("已购买", name_list[1], total_list.count(name_list[1]))
# 		print("已购买",name_list[2],total_list.count(name_list[2]))
# 		print("已购买", name_list[3], total_list.count(name_list[3]))
# 		print("剩余金额",salary)
# 		break
# 	else:
# 		buy_num = int(buy_num_input)  # 输入要买的商品编号
# 		buy_num -= 1
# 		if buy_num < 4:		#判断输入商品编号
# 			if price_list[buy_num] <= salary:		#判断是否买的起
# 				salary = salary - price_list[buy_num]		#购买并打印余额
# 				print("已将",name_list[buy_num],"加入购物车...","\n",
# 					  "花费金额",price_list[buy_num],"\n",
# 					  "剩余金额",salary)
# 				total_list.append(name_list[buy_num])		#将购买的商品放入购物列表
# 			else:
# 				balance = price_list[buy_num] - salary
# 				print("余额不足，还需金额",balance)
# 		else:
# 			print("输出错误，请重新输入")
# 			continue

#初始化变量、列表
# shopping_cart = []		#定义购物车
# price = [3800, 30, 50, 90]
# product = ["iphone", "coffee", "book", "condom"]
# flag = True
# salary = int( input("please input your salary:") )		#输入工资
#
# #列出商品
# for i in product:
# 	print(product.index(i) + 1, i, price[product.index(i)])
#
# while flag:
# 	while salary > 0:
# 		choice = input("please input the commodity number or 'q' to quit:")  # 输入购买的或者退出
# 		if choice == 'q':
# 			flag = False
# 			break
# 		if int(salary) < price[int(choice) - 1]:
# 			print("余额不足，还差%d"%(price[int(choice) - 1] - int(salary)))
# 		else:
# 			shopping_cart.append(product[int(choice) - 1])
# 			print(shopping_cart)
# 			salary = int(salary) - price[int(choice) - 1]
# 			print("您已购买%s,还剩金额%d"%(str(shopping_cart),salary))
# else:
# 	print("您已购买%s,还剩金额%d" % (str(shopping_cart), salary))


#初始化变量、列表
shopping_cart = {}		#定义购物车
product_list = [["iphone7",5800],
			    ["臭豆腐",100],
			    ["甜不辣",20],
			    ["拖鞋",50],
			    ["coffee",200]
			   ]
salary = int( input("please input your salary:") )		#输入工资

while True:
	num = 1
	for i in product_list:		#输出商品列表
		print(num,i)
		num += 1
	choice = input("请输入商品编号:").strip()			#输入商品编号
	if choice.isdigit():		#判断商品编号是否为数字
		choice = int(choice)
		if choice >= 1 and choice < 6:			#判断商品编号是否存在
			product = product_list[choice - 1]
			product_price = product[1]
			product_name = product[0]
			if product_price <= salary:			#判断能否买的起
				print("已购买商品%s"%(product_name))
				if product[0] in shopping_cart:		#判断购物车内是否存在商品
					shopping_cart[product[0]][1] += 1		#修改商品购买记录加入购物车
				else:
					shopping_cart[product[0]] = [product[1], 1]  # 创建商品购买记录加入购物车
				salary -= product_price
			else:
				balance = product_price - salary
				print("买不起，还差%d元"%(balance))
			print(shopping_cart)
		else:
			print("编号不存在，请重新输入!")
			continue
	elif choice == "q":
		print("---------您购买的商品如下---------")
		print("ID\t商品\t\t数量\t\t单价\t\t总价")
		id_num = 1
		total_cost = 0
		for i in shopping_cart:
			print("%s%10s%10s%10s%10s"%
				  (id_num,i,shopping_cart[i][1],shopping_cart[i][0],shopping_cart[i][1] * shopping_cart[i][0]))
			id_num += 1
			total_cost += shopping_cart[i][1] * shopping_cart[i][0]
		print("您已消费%d元"%(total_cost))
		print("您的余额为%d元"%(salary))
		print("------------退出购物-------------")
		break
	else:
		print("输出错误，请重新输入！")
		continue