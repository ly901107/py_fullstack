#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/21

# m = input('请输入要导入的模块：') #输入time
# m1 = __import__(m)
#
# print(m1)                       #<module 'time' (built-in)>
# print(m1.time())                #1511193808.3496895

import importlib

t = importlib.import_module('time')
print(t.time)                     #<built-in function time>
