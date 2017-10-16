#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/13

# import sys
# import time
#
# for i in range(100):
# 	sys.stdout.write("3#")
# 	sys.stdout.flush()
# 	time.sleep(0.5)

#---------------------------文件操作 查询
# while 1:
#
# 	url = input("please input url: ").strip()
# 	content = []
# 	flag = False
# 	with open("haproxy.conf", encoding="utf8") as f_read:
# 		for line in f_read:
# 			if line.startswith("backend") and url in line:
# 				flag = True
# 				continue
# 			if line.startswith("backend") and flag or line.startswith("data=input"):
# 				break
# 			if flag:
# 				content.append(line.strip())
# 		for i in content:
# 			print(i)

#---------------------------文件操作 打印进度条
# import sys
# import time
# for i in range(100):
# 	s = '\r%d%% %s' % (i,'#'*i)
# 	sys.stdout.write(s)
# 	sys.stdout.flush()
# 	time.sleep(0.5)

#----------------------------文件操作 文件复制并添加
count = 1
with open('text2',mode='r',encoding='utf8') as f_read,open('text3',mode='w',encoding='utf8') as f_write:
	for line in f_read:
		if count == 3:
			line = ''.join([line.strip(),'岳飞\n'])			#字符拼接
		f_write.write(line)
		count += 1
import os

os.rename('text2','text_bak')		#文件重命名
os.rename('text3','text2')
