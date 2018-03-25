#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/21

from threading import Thread,Lock
import time

def foo():

    global n

    lock.acquire()
    temp=n
    time.sleep(0.5)
    n=temp-1
    lock.release()

if __name__ == '__main__':

    n=100
    l=[]
    lock=Lock()

    for i in range(100):
        p=Thread(target=foo)
        l.append(p)
        p.start()

    for p in l:
        p.join()

    print(n)