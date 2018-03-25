#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/26

import socket

sock=socket.socket()
ip_port=('127.0.0.1',9000)
BUFSIZE=1024

sock.connect(ip_port)

while True:
    msg=input('>>>: ').strip()
    if not msg:continue
    sock.send(msg.encode('utf8'))
    msg=sock.recv(BUFSIZE)
    print(msg.decode('utf8'))

sock.close