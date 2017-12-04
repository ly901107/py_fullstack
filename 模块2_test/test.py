#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/23

# 字符集 字符编码

# n=u'老男孩'
#
# s = n.encode('gbk')	#gbk
#
# s.decode('gbk').encode('utf-8')	#utf-8

# globals()

# num = 2
# total = 0
#
# while num <= 100:
# 	if num % 2 != 0:
# 		total -= num
# 	else:
# 		total += num
# 	num += 1
# print(total)

# num =1
# while num <= 100:
# 	if num % 2 != 0:
# 		print(num)
# 	num += 1

# ss=("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
#
# ss[1][2]['k2'].append('number')
#
# print(ss)

# ss={"a":1,"b":2,"c":3}

# for key in ss:
# 	print(key)

# for key in ss.keys():
# 	print(key)

# c = a if 1 > 2 else b
#
# def func(arg):
# 	arg.append(55)
#
#
# li = [11, 22, 33, 44]
#
# li = func(li)
#
# print(li)

# temp_dict={"k1":"v1","k2":"v2"} #当做实参输入函数

#pass 意义


# def func(num):
#     if num > 33:
#         return True
#
#
# new_list = [11, 22, 33, 44, 55]
# a = filter(func, new_list)
# print(a)
# print(list(a))

# def func(arg):
#     arg.append(55)
#
#
# li = [11, 22, 33, 44]
#
# li = func(li)
#
# print(li)


# def foo():
#     print('foo')
#
# def bar(func):
#     # print(func)
#     return func
#
# f = bar(foo)
# print(f)

# def add():
#     print('==========function add')
#
# def    delete():
#     print('==========function delete')
#
# def search():
#     print('==========function search')
# def change():
#     print('==========function change')
#
# def tell_msg():
#     msg = '''
#     delete:删除
#     add:添加
#     search:查询
#     change:更改
#     '''
#     print(msg)
#
# cmd_list = {
#     'add':add,
#     'delete':delete,
#     'search':search,
#     'change':change
# }
#
# while True:
#     tell_msg()
#     choice = input('please input your choice: ').strip()
#     cmd_list[choice]()

# s = 'foo'
# d = {'a':1}
# def f():
#     s = 'bar'
#     d['b'] = 2
# f()
# print (s)
# print (d)

def foo():
    a = 1
    b = (1,2,3)
    c = {1:2,2:3}

# foo()
# print(a)
# print(b)
print(c)