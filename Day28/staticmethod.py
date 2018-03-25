#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/19

import time

class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod   #相当于给类扩展功能
    def now():      #用Date.now()形式去产生实例，该实例用的是当前时间
        t = time.localtime()    #获取结构化的时间格式
        obj = Date(t.tm_year,t.tm_mon,t.tm_mday)    #新建实例并且返回
        print('from now')
        return obj

    @staticmethod
    def tomorrow(): #用Date.tomorrow()形式去产生实例，该用例用的是明天的时间
        t = time.localtime(time.time()+86400)
        obj = Date(t.tm_year,t.tm_mon,t.tm_mday)
        return obj

# d1 = Date.now()
# print(d1.year,d1.month,d1.day)
# d2 = Date.tomorrow()
# print(d2.year,d2.month,d2.day)
# d1.now()        #TypeError: now() takes 0 positional arguments but 1 was given

d1 = Date(2012,12,12)
d1.now()
# d_n1 = Date.now()
# d_n2 = d1.now()
# print(d_n1.year,d_n1.month,d_n1.day)
# print(d_n2.year,d_n2.month,d_n2.day)
# Date.now()
