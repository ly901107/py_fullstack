#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/20

# import sys
#
# def s1():
#     print('s1')
#
#
# def s2():
#     print('s2')
#
# this_module = sys.modules[__name__]         #获取到当前模块
# print(this_module)                          #<module '__main__' from 'C:/Users/Administrator/PycharmProjects/py_fullstack/Day29/反射当前模块.py'>
#
# print(this_module.s1)                       #<function s1 at 0x00000000004E3F28>
# print(this_module.s2)                       #<function s2 at 0x0000000001E9A9D8>
# print(hasattr(this_module,'s1'))            #True
# print(getattr(this_module,'s2'))            #<function s2 at 0x000000000220A9D8>

import sys

def add():
    print('add')

def change():
    print('change')

while True:
    cmd = input('<<<<').strip()
    this_model = sys.modules[__name__]
    if hasattr(this_model,cmd):
        func = getattr(this_model,cmd)
        func()