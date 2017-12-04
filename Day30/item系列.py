#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/22

class Foo:
    def __init__(self, name):
        self.name = name
    def __getitem__(self, item):
        print(self.__dict__[item])
        print('from getitem')

    def __setitem__(self, key, value):
        self.__dict__[key] = value
        print('from setitem')

    def __delitem__(self, key):
        self.__dict__.pop(key)
        print('from delitem')

f = Foo('lex')
# print(f.__dict__)
# f['age'] = 18
# print(f.__dict__)
f['name']
del f['name']

