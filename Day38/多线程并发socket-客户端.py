#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/21

import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port=('127.0.0.1',9000)
BUFSIZE=1024

sock.connect(ip_port)

while True:
    msg=input('>>>: ').strip()
    if not msg:continue
    sock.send(msg.encode('utf-8'))
    msg_recv=sock.recv(BUFSIZE)
    print(msg_recv.decode('utf-8'))


