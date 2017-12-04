#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/23

import time
#--------------------------我们先以当前时间为准,让大家快速认识三种形式的时间
print(time.time()) # 时间戳:1487130156.419527
print(time.strftime("%Y-%m-%d %X")) #格式化的时间字符串:'2017-02-15 11:40:53'

print(time.localtime()) #本地时区的struct_time
print(time.gmtime())    #UTC时区的struct_time
