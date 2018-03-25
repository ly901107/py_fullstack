#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/21


from threading import Thread,Lock
import time

mutexA=Lock()
mutexB=Lock()

class MyThread(Thread):

    def __init__(self):
        super().__init__()

    def run(self):
        self.fun1()
        self.fun2()

    def fun1(self):
        mutexA.acquire()
        print('fun1 get mutexA',self.name)

        mutexB.acquire()
        print('fun1 get mutexB',self.name)

        mutexB.release()

        mutexA.release()

    def fun2(self):
        mutexA.acquire()
        print('fun2 get mutexA',self.name)

        time.sleep(0.2)

        mutexB.acquire()
        print('fun2 get mutexB',self.name)

        mutexB.release()

        mutexA.release()

if __name__ == '__main__':
    print('---start---')
    for i in range(10):
        t=MyThread()
        t.start()