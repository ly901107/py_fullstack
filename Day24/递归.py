#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/30

# def age(n):
# 	if n == 1:
# 		return 10
# 	else:
# 		return age(n-1)+2
#
# print(age(5))

l=[1,2,10,30,33,99,101,200,301,402]

def search(num,date):
    if len(date)/2 >1:
        mid_index=int(len(date)/2)		#获取列表中间位置
        mid_value=date[mid_index]		#获取列表中间值
        if num > mid_value:
            'num在列表的右边'
            date=date[mid_index:]
            search(num,date)
        elif num < mid_value:
            'num在列表的左边'
            date=date[:mid_index]
            search(num,date)
        else:
            print('找到了')
            return
    else:
        if date[0] == num:
            print('找到了')
        else:
            print('不存在')

search(31,l)


