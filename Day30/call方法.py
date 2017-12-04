#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/23

class Foo:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('from call')

f = Foo()
f()
