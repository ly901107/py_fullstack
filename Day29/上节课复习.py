#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/20

class People:
    def __init__(self,name,x):
        self.name = name
        self.__SEX = x

    @property
    def sex(self):
        return self.__SEX

p1 = People('lex','male')
print(p1.sex)                 #male