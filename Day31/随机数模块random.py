#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/23

import random

def foo():

    s = ''

    for i in range(5):
        rNum = random.randint(0,9)

        rLetter = chr(random.randint(65,90))
        rLetter1 = chr(random.randint(97,122))
        res = random.choice([str(rNum),rLetter,rLetter1])
        s += res
    return s

print(foo())
