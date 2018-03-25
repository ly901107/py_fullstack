#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/7

import socket
import struct

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port = ('192.168.31.66',8080)
BUFSIZE = 1024

s.connect(ip_port)

while True:
    msg = input('>>: ').strip()
    if not msg:continue
    if msg == 'quit':continue
    s.send(bytes(msg.encode('utf-8')))

    #收报头
    baotou = s.recv(4)
    datesize = struct.unpack('i',baotou)[0]

    #收数据
    recv_size = 0
    recv_date = b''
    while recv_size < datesize:
        date = s.recv(BUFSIZE)
        recv_size += len(date)
        recv_date += date

    print(recv_date.decode('gbk'))
s.close
