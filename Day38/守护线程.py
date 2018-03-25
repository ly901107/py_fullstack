#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/21

# 示例1
# from threading import Thread
# import time
#
# def foo(name):
#     time.sleep(2)
#     print('%s say hello'% name)
#
# if __name__ == '__main__':
#
#     t=Thread(target=foo,args=('name',))
#     t.setDaemon(True)
#     t.start()
#
#     print('主线程')
#     time.sleep(1)
#     print(t.is_alive())


#示例2

from threading import Thread
import time
def foo():
    print(123)
    time.sleep(3)
    print("end123")

def bar():
    print(456)
    time.sleep(2)
    print("end456")

if __name__ == '__main__':
    t1=Thread(target=foo)
    t2=Thread(target=bar)

    t1.setDaemon(True)

    t1.start()
    t2.start()

    print('main')