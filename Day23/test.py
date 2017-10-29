#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/29



# a = [1,2,3]
# b = [4,5,6]
# c = [4,5,6,7,8]
# zipped = zip(a,b)    # zipped 为迭代器
# for i in zipped:
# 	print(i)
#
# # (1, 4)
# # (2, 5)
# # (3, 6)


# salaries={
#     'egon':3000,
#     'alex':100000000,
#     'wupeiqi':10000,
#     'yuanhao':2000
# }
#
#
# print(sorted(salaries))		#默认是按照字典salaries的key去排序 ['alex', 'egon', 'wupeiqi', 'yuanhao']
# print(sorted(salaries,key=lambda k:salaries[k]))	['yuanhao', 'egon', 'wupeiqi', 'alex']

# def extendList(val, list=[]):
# 	list.append(val)
# 	return list
#
#
# list1 = extendList(10)
# print("list1 = %s" % list1)
# list2 = extendList(123, [])
# print("list2 = %s" % list2)
# list3 = extendList('a')
# print("list3 = %s" % list3)
#
# print("list1 = %s" % list1)
#
# print("list2 = %s" % list2)
#
# print("list3 = %s" % list3)

# list = ['a', 'b', 'c', 'd', 'e']
# print(list[10:])
# def multipliers():
# 	return ['a','b','c','d']
# print ([m(2) for m in range(5)])

def multipliers():
    return (lambda x : i*x for i in range(4))

print ([m(2) for m in multipliers()] )

# output:
# [6, 6, 6, 6]

# def create_multipliers():
#     return (lambda x : i * x for i in range(5))
# for multiplier in create_multipliers():
#     print (multiplier(2))
