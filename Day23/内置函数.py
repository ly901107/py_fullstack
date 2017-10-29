#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/29

# print(bytes('hello',encoding='utf-8'))	#将字符串转换成字节形式，可指定字符编码
# print(callable(sum))	#检测一个对象是否可以被调用
# print(chr(65))	#返回ASCII码对应字符
# print(ord('A'))	#返回ASCII码对应的数字
# complex()	#创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数
# dir()	#不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表
# divmod()	#把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
# enumerate()		#同时列出数据和数据下标，一般用在 for 循环当中
# hash()	#获取取一个对象（字符串或者数值等）的哈希值,一般用于校验，哈希值不能逆推
# hex()	#十进制转十六进制
# id()	#可以返回一个对象的身份，返回值为整数


# #max 和 min
# salaries={
#     'egon':3000,
#     'alex':100000000,
#     'wupeiqi':10000,
#     'yuanhao':2000
# }
#
# def get_value(key):
# 	return salaries[key]
#
# print(max(salaries))		#max进行比较时，默认按照字典的key去比较,得到的返回值也是字典的key
# print(max(salaries,key = get_value))
# #max会将前面的可迭代对象变成生成器，每次next，将返回值传给后面的参数get_value;
# #函数get_value返回key对应的值，赋值给key，然后会按照key进行比较
#
#
# #匿名函数
# lambda key:salaries[key]
# #等同于
# def get_value(key):
# 	return salaries[key]
#
# # 上面的max函数可以用匿名函数实现
# print(max(salaries, key=lambda key:salaries[key]))
#
# #数据类型
# int
# num = 1		#num = int(1)
# print(type(num))	#查看num的类型	<class 'int'>
# print(isinstance(num,int))		#判断num是否为int类型		True
# print(num is 1)		#is 是身份运算，根据id去判断身份	True
#
# str
# list
# x = []
# x = list(i for i in rang(10))
# tuple
#
# dict
# d = {'a':1 }
# d = dict(a=1)		#工厂函数,等价于上面
#
# set
# frozenset	#不可变集合
#
# #在面向对象里面讲
# classmethod
# staticmethod
# property
# delattr()
# hasattr()
# getattr()
# setattr()
# issubclass()
# super()



# # 字节码
# compile()
# eval()
# exec()

#sorted
# l=[3,4,1,0,9,8]
# print(sorted(l))	#返回值是列表，默认是升序
# print(sorted(l,reverse=True))	#降序排列
#
# s='hello world'
# print(sorted(s))

#map
# l=[1,3,5,2,0]
# m=map(lambda k:k**2,l)
# print(list(m))		#[1, 9, 25, 4, 0]
#
# name_l=['alex','zhejiangF4','wupeiqi','yuanhao']
# m=map(lambda name:name+'SB',name_l)
# print(list(m))		#['alexSB', 'zhejiangF4SB', 'wupeiqiSB', 'yuanhaoSB']

# #reduce
#
# from functools import reduce
# l=list(range(100))	#生成一个1到100的列表
# print(reduce(lambda x,y:x+y,l))		#reduce 还有默认参数 用法不是很理解

#filter
#
# name_l=[
# 	{'name':'egon','age':18},
# 	{'name':'alex','age':1000},
# 	{'name':'wupeiqi','age':2000}
# ]

# f=filter(lambda d:d['age']>100,name_l)
# for i in f:
# 	print(i)

oct()	#十进制转八进制

pow(x,y,z)	#返回 xy（x的y次方)的值，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z
reversed()	#返回一个反转的迭代器,不修改原对象
round()		#返回浮点数x的四舍五入值
#slice
slice()		#切片
l=[1,2,3,4]
print(l[1:3])

s=slice(1,3)
print(l[s])
#vars
vars()	#没有参数，就打印当前调用位置的属性和属性值 类似 locals()
# __import__()
import time
print(time)

m=__import__('time')		#通过字符串导入模块
print(m)