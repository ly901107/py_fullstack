#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/26

def add():
	print('==========function add')

def	delete():
	print('==========function delete')

def search():
	print('==========function search')
def change():
	print('==========function change')

def tell_msg():
	msg = '''
	delete:删除
	add:添加
	search:查询
	change:更改
	'''
	print(msg)

cmd_list = {
	'add':add,
	'delete':delete,
	'search':search,
	'change':change
}

while True:
	tell_msg()
	choice = input('please input your choice: ').strip()
	cmd_list[choice]()