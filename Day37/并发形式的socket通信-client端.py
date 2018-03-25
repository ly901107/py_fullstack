#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/20

import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port=('127.0.0.1',9000)
BUFSIZE=1024

client.connect(ip_port)

while True:
    msg=input('>>>: ').strip()
    if not msg:
        continue
    client.send(msg.encode('utf-8'))
    msg_recv=client.recv(BUFSIZE)
    print(msg_recv.decode('utf-8'))

client.close