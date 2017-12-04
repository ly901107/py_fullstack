#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/20

# class Foo:
#     pass
#
# obj = Foo()
#
# print(isinstance(obj,Foo))      #True

class Foo:
    pass

class Bar(Foo):
    pass

print(issubclass(Bar,Foo))        #True