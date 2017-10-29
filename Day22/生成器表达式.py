#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/28

#
# res = []
# d = {}
#
#
# 	for line in f:
# 		l = line.split()
# 		d['name'] = l[0]
# 		d['price'] = l[1]
# 		d['num'] = l[2]
# 		res.append(d)
# print(res)


with open('b.txt','r',encoding='utf-8') as f:
	res = (line.split() for line in f)
	dic_g = ({'name':line[0],'price':line[1],'num':line[2]} for line in res)
	goods_dic = next(dic_g)
	print(goods_dic['num'])