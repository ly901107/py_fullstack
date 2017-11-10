#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/1

import os

def init(inputer1,inputer2,inputer3):
	'装饰器'
	'''
		inputer1为input的内容，inputer3为输入字符长度
		从文件中取出每一条记录放入列表info中，
		{'staff_id': '1', 'name': 'Alex Li', 'age': '22', 'phone': '13651054608',
		 'dept': 'IT', 'enroll_date': '2013-04-01\n'}
	'''
	def init1(func):
		def init2():
			print('=========初始化==========')
			global user_list,info
			user_input = input(inputer1).strip()		#请求用户输入
			user_list = user_input.split(inputer2)		#输入内容以空格 拆分为列表
			with open('staff_info') as f:
				items = (line.split(',') for line in f)
				info = [{'staff_id': staff_id, 'name': name, 'age': age,
						 'phone': phone, 'dept': dept, 'enroll_date': enroll_date} \
						for staff_id, name, age, phone, dept, enroll_date in items]
			if len(user_list) == inputer3:	#防止输入错误报错
				func()
			else:
				print('输入格式错误，请重新输入')
		return init2
	return init1

@init('请输入模糊查询内容: ',' ',8)
def search():
	'查询员工信息'
	'''
		select name,age from staff_table where age > 22,
		select * from staff_table where dept = "IT",
		select * from staff_table where enroll_date like "2013"
	'''
	found_info = []		#最终查询到的内容
	if user_list[5] == 'age' and user_list[6] == '>':	#判断输入是否正确
		found_info=[key for key in info if int(key['age'])>int(user_list[7])]	#遍历列表info,将查询到的内容放入列表中
	elif user_list[5] == 'dept' and user_list[6] == '=':
		found_info=[key for key in info if key['dept'] in user_list[7]]
	elif user_list[5] == 'enroll_date' and user_list[6] == 'like':
		found_info = [key for key in info if key['enroll_date'][0:4] in user_list[7]]
	print(found_info if len(found_info) > 0 else '没有找到')		#判断是否找到
	print('查询到%s条信息'%(len(found_info)))

@init('请输入增加内容: ',',',5)
def add():
	'增加员工信息'
	'''
	注释信息：
			可创建新员工纪录，以phone做唯一键，staff_id需自增
			name,age,phone,dept,enroll-date
			例如：mengzhu,23,12345678901,IT,2013-04-01
	'''
	add_info=[key for key in info if str(user_list[2]) == key['phone']]	#遍历列表info,添加符合输入phone的信息到add_info
	if add_info:
		print('phone已存在')
	else:
		user_list.insert(0,str(len(info) + 1))	#staff_id自增
		add_list=','.join(user_list)	#列表中增加','
		with open('staff_info','a+') as f:
			f.write('\n')
			for i in add_list:
				f.write(i)

@init('请输入删除员工id号: ',' ',1)
def delete():
	'删除员工信息'
	'''
	注释信息：
			可删除指定员工信息纪录，输入员工id，即可删除
	'''
	del_info = [key for key in info if str(user_list[0]) == key['staff_id']]
	if del_info:
		print('已找到，正在删除')
		with open('staff_info') as f_read, open('.bak.txt', 'w') as f_write:
			for line in f_read:
				if user_list[0] == line.split(',')[0]:
					continue
				else:
					f_write.write(line)
		os.remove('staff_info')
		os.rename('.bak.txt','staff_info')
	else:
		print('未找到')

@init('请输入修改员工信息: ',' ',11)
def change():
	'修改员工信息'
	'''
	注释信息：
			可修改员工信息，语法如下:
			UPDATE staff_table SET dept = "Market" WHERE where dept = "IT"
	'''
	change_info = [key for key in info if key['dept'] in user_list[10]]
	if change_info:
		print('已找到，正在修改')
		with open('staff_info') as f_read, open('.bak.txt', 'w') as f_write:
			for line in f_read:
				change_list = line.split(',')
				if change_list[4] in user_list[10]:		#查找符合输入的行
					change_list[4] = user_list[5].strip('"')	#将源文件的IT替换为Market
				change_list = ','.join(change_list)
				for i in change_list:
					f_write.write(i)
		os.remove('staff_info')
		os.rename('.bak.txt','staff_info')
	else:
		print(print('未找到'))

def tell_msg():
	'选项菜单打印信息'
	msg='''
1.增加员工
2.删除员工
3.修改员工
4.模糊查询
5.退出
'''
	print(msg)

while True:
	'''
	注释信息：
			选项菜单程序,用户进行菜单选择
			输入'1','2','3','4','5' 分别对应 
			增加、删除、修改、查询、退出功能
			输入错误提示重新输入
	'''
	tell_msg()
	cmd_list = {
		'1': add,
		'2': delete,
		'3': change,
		'4': search
	}
	user_choice = input('请输入您要操作的选项序号: ').strip()
	if user_choice == '5':
		exit('已退出，谢谢使用')
	elif user_choice in cmd_list:
		cmd_list[user_choice]()
	else:
		print('输入错误,请重新输入!')
		continue