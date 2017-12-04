#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/21

class Foo:
    x = 1

    def __init__(self, y):
        print('====66======')
        self.y = y
        print('============')

    def __getattr__(self, item):
        print('----> from getattr:你找的属性不存在')

    def __setattr__(self, key, value):
        print('----> from setattr')
        # self.key=value #这就无限递归了,你好好想想
        self.__dict__[key]=value #应该使用它

    def __delattr__(self, item):
        print('----> from delattr')
        # del self.item #无限递归了
        self.__dict__.pop(item)


# __setattr__添加/修改属性会触发它的执行
f1 = Foo(10)        #----> from setattr
print(f1.__dict__)  #{'y': 10} 因为你重写了__setattr__,凡是赋值操作都会触发它的运行,你啥都没写,就是根本没赋值,
# 除非你直接操作属性字典,否则永远无法赋值
f1.z = 3            #----> from setattr
print(f1.__dict__)  #{'y': 10, 'z': 3}


f1.__dict__['a']=3  #----> from setattr 我们可以直接修改属性字典,来完成添加/修改属性的操作
del f1.a            #----> from delattr
print(f1.__dict__)  #{'y': 10}

