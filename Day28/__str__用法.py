#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/19


class foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return '<name:%s,age:%s>'%(self.name,self.age)

f1 = foo('lex',18)
print(f1)           #<name:lex,age:18>
