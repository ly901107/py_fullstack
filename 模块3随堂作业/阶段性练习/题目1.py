#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/31

# 1.文件内容如下,标题为:姓名,性别,年纪,薪资
#     egon male 18 3000
#     alex male 38 30000
#     wupeiqi female 28 20000
#     yuanhao female 28 10000
#     要求:
#     从文件中取出每一条记录放入列表中,
#     列表的每个元素都是{'name':'egon','sex':'male','age':18,'salary':3000}的形式

with open('salary',encoding='utf-8') as f:
	items = (line.split() for line in f)
	info = [{'name':name,'sex':sex,'age':age,'salary':salary} for name,sex,age,salary in items]
	# print(info)
# # 2 根据1得到的列表,取出薪资最高的人的信息
#
# # print(max(info,key=lambda k:k['salary']))
#
# #3 根据1得到的列表,取出最年轻的人的信息
print(min(info,key=lambda k:['age']))
#
# #4 根据1得到的列表,将每个人的信息中的名字映射成首字母大写的形式
# info_new=map(lambda k:{'name':k['name'].capitalize(),'sex':k['sex'],'age':k['age'],'salary':k['salary']},info)
# # print(list(info_new))
#
# #5根据1得到的列表,过滤掉名字以a开头的人的信息
# info5=filter(lambda k: not k['name'].startswith('a'),info)
# print(list(info5))
