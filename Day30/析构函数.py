#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/22

class Open:
    def __init__(self, filepath, mode = 'r', encode = 'utf-8'):
        self.f = open(filepath, mode= mode, encoding= encode)

    def write(self,value):
        print('=======')
        self.f.write(value)

    def __getattr__(self, item):
        return getattr(self.f, item)

    def __del__(self):
        print('from del')
        self.f.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# with Open('a.txt','r+') as f_write:
#     f_write.write('aaaa6666aaaaaaaa\n')


f = Open('a.txt','r+')
# f.write('aaaaaaaaaaaaaaaaaa')
print(f.__dict__)
