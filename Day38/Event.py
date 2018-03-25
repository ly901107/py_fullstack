#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/21

#有多个工作线程尝试链接MySQL，我们想要在链接前确保MySQL服务正常才让那些工作线程去连接MySQL服务器，
# 如果连接不成功，都会去尝试重新连接。那么我们就可以采用threading.Event机制来协调各个工作线程的连接操作


from threading import Thread,Event
import time,threading

def conn_mysql():
    count=1
    while not event.is_set():
        print('<%s>第%s次尝试连接'%(threading.current_thread().getName(),count))
        event.wait(0.5)
        count += 1

    print('<%s>链接成功'%(threading.current_thread()))

def check_mysql():
    time.sleep(1)
    event.set()

if __name__ == '__main__':

    event=Event()

    conn1=Thread(target=conn_mysql)
    conn2=Thread(target=conn_mysql)
    check=Thread(target=check_mysql)

    conn1.start()
    conn2.start()
    check.start()


# <Thread-1>第1次尝试连接
# <Thread-2>第1次尝试连接
# <Thread-1>第2次尝试连接
# <Thread-2>第2次尝试连接
# <<Thread(Thread-1, started 99548)>>链接成功
# <<Thread(Thread-2, started 102636)>>链接成功