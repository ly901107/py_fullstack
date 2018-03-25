#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/7

#简单版
# import socket
#
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# ip_port = ('127.0.0.1',9000)
# BUFSIZE = 1024
#
# s.connect(ip_port)                                      #拨电话
#
# s.send('lex'.encode('utf-8'))                           #发消息，只能发送字节类型
#
# msg = s.recv(BUFSIZE)                                   #收消息，听话
#
# print(msg.decode('utf-8'))
#
# s.close()


#改进版

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port = ('127.0.0.1',9000)
BUFSIZE = 1024

s.connect_ex(ip_port)
while True:
    msg = input('>>>: ').strip()
    if not msg:continue
    s.send(msg.encode('utf-8'))

    feedback = s.recv(BUFSIZE)
    print(feedback)
    print(feedback.decode('utf-8'))
s.close