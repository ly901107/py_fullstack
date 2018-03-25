#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/24

# import threading
# import time
#
# class MyThread(threading.Thread):
#
#     def __init__(self,num):
#         threading.Thread.__init__(self)
#         self.num=num
#
#     def run(self):
#         print("running on number:%s" %self.num)
#         time.sleep(3)
#
# t1=MyThread(56)
# t2=MyThread(78)
#
# t1.start()
# t2.start()
# print("ending")


import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)

def worker(event):
    logging.debug('Waiting for redis ready...')
    event.wait()
    logging.debug('redis ready, and connect to redis server and do some work [%s]', time.ctime())
    time.sleep(1)

def main():
    readis_ready = threading.Event()
    t1 = threading.Thread(target=worker, args=(readis_ready,), name='t1')
    t1.start()

    t2 = threading.Thread(target=worker, args=(readis_ready,), name='t2')
    t2.start()

    logging.debug('first of all, check redis server, make sure it is OK, and then trigger the redis ready event')
    time.sleep(3) # simulate the check progress
    readis_ready.set()

if __name__=="__main__":
    main()