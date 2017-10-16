#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/14

# 三级菜单：
#     1. 运行程序输出第一级菜单
#     2. 选择一级菜单某项，输出二级菜单，同理输出三级菜单
#     3. 返回上一级菜单和顶部菜单
#     4. 菜单数据保存在文件中


current_layer = {}
last_layers = []		#定义最后一层
with open('menu',encoding='utf8') as f_menu:
	f_read = f_menu.read()		#将文件信息全部读取出来
	f_read_str = str(f_read)		#转换成字符串
current_layer = eval(f_read_str)		#转换成字典


while True:
	for key in current_layer:
		print(key)
	choice = input('Please input your choice: ').strip()
	if len(choice) == 0:		#保证输入不为空
		continue
	if choice in current_layer and isinstance(current_layer, dict):		#判断输入是否在当前层，并且当前层为字典
		last_layers.append(current_layer)		#将当前层加入到列表中
		current_layer = current_layer[choice]		#进入下一层
	if choice == 'b':		#返回上一层
		if last_layers:		#保证列表不为空
			current_layer = last_layers.pop()		#取上一层为当前层并且删除列表最后一个
	if choice == 'top':		#返回顶层
		current_layer = last_layers[0]
		last_layers = []
	if choice == 'q':		#退出
		break
#666666
	print("6666")

