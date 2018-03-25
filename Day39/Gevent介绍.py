#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/23

#遇到IO阻塞时会自动切换任务

# import gevent
# import time
#
# def eat(name):
#     print('%s eat 1'%name)
#     gevent.sleep(2)
#     print('%s eat 2'%name)
#
# def play(name):
#     print('%s play 1'%name)
#     gevent.sleep(2)
#     print('%s play 2'%name)
#
# start=time.time()
# g1=gevent.spawn(eat,'egon')
# g2=gevent.spawn(play,name='lex')
#
# gevent.joinall([g1,g2])
#
# print('主',time.time()-start)
#
# # egon eat 1
# # lex play 1
# # egon eat 2
# # lex play 2
# # 主 2.0011146068573

#执行到IO操作时，gevent自动切换

from gevent import monkey;monkey.patch_all()

import gevent,time

def eat(name):
    print('%s eat 1'%name)
    time.sleep(1)
    print('%s eat 2'%name)

def play(name):
    print('%s play 1'%name)
    time.sleep(1)
    print('%s play 2'%name)

g1=gevent.spawn(eat,'lex')
g2=gevent.spawn(play,'egon')

gevent.joinall([g1,g2])
print('主')