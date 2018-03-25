#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/20

#方式1
# from threading import Thread
# import time
#
# def foo(name):
#     time.sleep(2)
#     print('%s say hello'%name)
#
# if __name__ == '__main__':
#     s=Thread(target=foo,args=('egon',))
#     s.start()
#     print('主线程')

# 主线程
# egon say hello

#方式2
from threading import Thread
import time

class Foo(Thread):

    def __init__(self, name):
        super().__init__()
        self.name=name

    def run(self):
        time.sleep(2)
        print('%s say hello'% self.name)

if __name__ == '__main__':
    f=Foo('egon')
    f.start()
    print('主线程')

# 主线程
# egon say hello