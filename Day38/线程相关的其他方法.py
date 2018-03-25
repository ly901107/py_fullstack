#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/21

from threading import Thread
import threading
import time

def work():
    time.sleep(2)
    print(threading.current_thread().getName())


if __name__ == '__main__':
    t=Thread(target=work)
    t.start()
    print(threading.current_thread().getName())
    print(threading.current_thread())
    print(threading.enumerate())
    print(threading.active_count())
    print('主线程')

# MainThread
# <_MainThread(MainThread, started 57052)>
# [<_MainThread(MainThread, started 57052)>, <Thread(Thread-1, started 57484)>]
# 2
# 主线程
# Thread-1