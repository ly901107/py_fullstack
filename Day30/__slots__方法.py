#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/22

# class Foo:
#     __slots__ = 'x'
#
#
# f1 = Foo()
# f1.x = 1
# # f1.y = 2  # 报错
# print(f1.__slots__)  # f1不再有__dict__
# print(f1.__slots__)

# class Bar:
#     __slots__ = ['x', 'y']
#
#
# n = Bar()
# n.x, n.y = 1, 2
# n.z = 3  # 报错

class Foo:
    __slots__ = ['name', 'age']


f1 = Foo()
f1.name = 'alex'
f1.age = 18
print(f1.__slots__)

f2 = Foo()
f2.name = 'egon'
f2.age = 19
print(f2.__slots__)

print(Foo.__dict__)