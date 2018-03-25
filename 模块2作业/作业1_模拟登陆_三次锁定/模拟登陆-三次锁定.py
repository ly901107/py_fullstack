#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/14

#  1、使用while循环输入 1 2 3 4 5 6     8 9 10
#     2、求1-100的所有数的和
#     3、输出 1-100 内的所有奇数
#     4、输出 1-100 内的所有偶数
#     5、求1-2+3-4+5 ... 99的所有数的和
# 模拟登陆
#     1. 用户输入帐号密码进行登陆
#     2. 用户信息保存在文件内
#     3. 用户密码输入错误三次后锁定用户


#----------1、使用while循环输入 1 2 3 4 5 6     8 9 10

count = 0
while count<10:
	number = input('>>>').strip()
	print(number)
	count += 1

#----------2、求1-100的所有数的和

sum = 0
for i in range(101):
	sum += i
print(sum)
#----------2、求1-100的所有数的和 优化

print(sum(range(1,101)))

#----------3、输出 1-100 内的所有奇数

for i in range(101):
	if i % 2 != 0:		#取余 判断是否为奇数数
		print(i)

#----------4、输出 1-100 内的所有偶数

for i in range(101):
	if i % 2 == 0:		#取余 判断是否为偶数
		print(i)

#----------5、求1-2+3-4+5 ... 99的所有数的和

sum = 0
for i in range(1,100):
	if i % 2 == 0:
		i = -i
	sum += i
print(sum)

#---------6、模拟登陆
#     		1. 用户输入帐号密码进行登陆
#     		2. 用户信息保存在文件内
#     		3. 用户密码输入错误三次后锁定用户

import sys
passwd_wrong = []
count = 0
flag_count = True
flag_login = False

while flag_count:
    username = input('please input your username: ').strip()		#输入用户名
    with open('lock_user','r', encoding='utf8') as f_lock:
        for line in f_lock:
            if username == line.strip():		#判断用户名是否被锁定
                sys.exit('%s 已经被锁定'%username)		#退出主程序并打印

    count = passwd_wrong.count(username)  # 判断用户名输入次数

    if count < 3:  # 判断此用户名是否已登陆3次
        passwd = input('please input your passwd: ').strip()		#输入密码
        with open('user_passwd','r',encoding='utf8') as f_user:
            for line in f_user:
                f_username,f_passwd = line.strip().split()		#遍历出的用户名密码进行赋值操作
                if username == f_username and passwd == f_passwd:		#判断输入的用户名密码是否存在
                    flag_login = True
                    print('登陆成功')
                    break
            if flag_login:		#判断是否登陆成功
                break
            else:			#登陆失败
                passwd_wrong.append(username)		#将登陆失败用户名加入列表中
                count = passwd_wrong.count(username)		#计算此从户名登陆次数
                print('密码错误，还剩下%s次机会'%(3-count))
                if count == 3:
                    flag_count = False
    else:
        flag_count = False
else:
    with open('lock_user','a+',encoding='utf8') as f_lock:
        f_lock.write(username+'\n')
        print('用户名%s输入次数过多，已被锁定'%username)
