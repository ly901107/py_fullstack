#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/2

#spam.py
print('from the spam.py')

money=1000

def read1():
    print('spam模块：',money)

def read2():
    print('spam模块')
    read1()

def change():
    global money
    money=0