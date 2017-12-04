#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/23


# class Foo:
#     x = 1
#
#     def __init__(self):
#         pass
#
#     def foo(self):
#         pass
#
# # print(Foo.__dict__)
#
#
# f = Foo()
#
# print(f.__dict__)


# class_name = 'lex'
# class_base = (object,)
# class_dict = {
#     'x':1
# }
#
# f = type(class_name, class_base, class_dict)
# print(f.__dict__)


g={
    'x':1,
    'y':2,
    'teachers':{'egon','alex','yuanhao','wupeiqi'}
}
l={'birds':[1,2,3]}

# exec("""
# def func():
#     global x
#     x='egon'
# func()
# """,g,l)
# print(g)
# print(l)

exec("""
global x
x='egon'
""",g,l)
print(g)
# print(l)