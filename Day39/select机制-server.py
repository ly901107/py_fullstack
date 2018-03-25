#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/26


import socket,select

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port=('127.0.0.1',9000)
BUFSIZE=1024

sock.bind(ip_port)
sock.listen(5)

# sock.setblocking(False)

inputs=[sock,]

while True:
    r,w,x=select.select(inputs,[],[])

    for obj in r:
        if obj == sock:
            conn,addr=obj.accept()
            inputs.append(conn)
        else:
            msg=obj.recv(BUFSIZE)
            print(msg.decode('utf8'))
            send_msg=input('>>>: ').strip()
            obj.send(send_msg.encode('utf8'))



