#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/7

#简单版
# import socket
#
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)        #买手机
# ip_port = ('127.0.0.1',9000)                                #电话卡
# BUFSIZE = 1024                                              #收发消息的尺寸
#
# s.bind(ip_port)                                            #手机插卡
# s.listen(5)                                                 #手机待机
#
# conn,addr = s.accept()                                      #接电话
# print(conn)
# print(addr)
#
# msg = conn.recv(BUFSIZE)                                    #听消息，听话
# print(msg,type(msg))
#
# conn.send(msg.upper())                                      #发消息，说话
#
# conn.close()                                                #挂电话
#
# s.close()                                                   #关机


#改进版

import  socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port = ('127.0.0.1',9000)
BUFSIZE = 1024

s.bind(ip_port)
s.listen(5)

while True:
    conn,addr = s.accept()
    print('conn',conn)
    print('addr',addr)
    while True:
        try:    #windows
            msg = conn.recv(BUFSIZE)
            # if len(msg) == 0:break    #linux
            print('接受消息',msg)
            print(msg.decode('utf-8'))
            conn.send(msg.upper())
        except Exception:
            break
    conn.close
s.close
