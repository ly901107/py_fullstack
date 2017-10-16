#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/3

set1 = {"123","234","345","456","567","678"}
set2 = {"789","678","567","666","888"}


print(set1.intersection(set2))		#交集
print(set1 & set2 )		#交集
print(set1.difference(set2))		#差集
print(set1 - set2)		#差集
print(set1.union(set2))		#并集
print(set1 | set2)		#并集
print(set1.symmetric_difference(set2))		#对称差集
print(set1.update(set2))	#将set2合并到set1当中
print(set1.add("000"))		#增加
print(set1.difference_update(set2))		#求差集
set1.discard("123")		#删除
print(set1)
print(set1.issubset(set2))
print(set1.issuperset(set2))