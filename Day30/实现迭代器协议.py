#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/22

# class Foo:
#     def __init__(self,start):
#         self.start = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         n = self.start
#         if self.start > 10:
#             raise StopIteration
#         self.start += 1
#         return n
#
# f = Foo(0)
#
# for i in f:
#     print(i)

class Range:
    def __init__(self,start,stop,step):
        self.start = start
        self.stop = stop
        self.setp = step

    def __iter__(self):
        return self

    def __next__(self):

        if self.start == self.stop:
            raise StopIteration
        index = self.start
        self.start += self.setp
        return index

for i in Range(1,10,1):
    print(i)