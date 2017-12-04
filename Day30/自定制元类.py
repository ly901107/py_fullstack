#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/23


class Mymeta(type):
    def __init__(self, class_name, class_bases, class_dic):
        pass

    def __call__(self, *args, **kwargs):
        obj = self.__new__(self)                #产生一个空对象obj
        self.__init__(obj, *args, **kwargs)     #obj.name = 'lex'   实例化的时候会调用init方法
        return obj

class Foo(metaclass=Mymeta):
    x = 1
    def __init__(self, name):
        self.name = name

    def run(self):
        print('%s is running'%self)

f = Foo('lex')
print(f)
