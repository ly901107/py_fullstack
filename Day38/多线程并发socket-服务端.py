#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/21

from threading import Thread
import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port=('127.0.0.1',9000)
BUFSIZE=1024

sock.bind(ip_port)
sock.listen(5)

def action(conn):
    while True:
        try:
            date=conn.recv(BUFSIZE)
            print(date.decode('utf-8'))
            msg=input('>>>: ').strip()
            conn.send(msg.encode('utf8'))
        except Exception:
            break


if __name__ == '__main__':

    while True:
        conn,addr=sock.accept()
        p=Thread(target=action,args=(conn,))
        p.start()