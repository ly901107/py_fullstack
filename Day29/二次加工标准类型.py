#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/21
#
# class List(list):
#     def append(self, object):
#         if not isinstance(object, int):
#             raise TypeError('must be int')
#         super().append(object)
#
# l = List([1,2,3])
# print(l)
# l.append(123)
# print(l)
# l.append('123')     #TypeError: must be int


# def test(x:int, y:int):
#     return x + y
#
# print(test(1,2))
# print(test(1,'2'))


# class List(list):
#     def insert(self, index: int, object):

# import time
#
# t = time.strftime('%Y-%m-%d %X')        #2017-11-21 22:00:33
# print(t)

import time
class FileHandle:
    def __init__(self,filename,mode='r',encoding='utf-8'):
        self.file=open(filename,mode,encoding=encoding)
    def write(self,line):
        t=time.strftime('%Y-%m-%d %T')
        self.file.write('%s %s' %(t,line))

    def __getattr__(self, item):
        return getattr(self.file,item)

f1=FileHandle('b.txt','w+')
f1.write('你好啊')
f1.seek(0)
print(f1.read())            #2017-11-21 23:18:55 你好啊
f1.close()
