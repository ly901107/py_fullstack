#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/20


import socket
from multiprocessing import Process

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ip_port=('127.0.0.1',9000)
BUFSIZE=1024

server.bind(ip_port)
server.listen(5)

def talk(conn,addr):
    while True:
        try:
            msg=conn.recv(BUFSIZE)
            print(msg.decode('utf-8'))
            conn.send(msg.upper())
        except Exception:
            break

    conn.close


if __name__ == '__main__':
    while True:
        conn,addr=server.accept()
        t=Process(target=talk,args=(conn,addr))
        t.start()

    server.close