#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/26

# import selectors,socket
#
# sel=selectors.DefaultSelector()
#
# def read(conn,mask):
#     try:
#         msg=conn.recv(1024)
#         print(msg.decode('utf8'))
#         msg=input('>>>: ').strip()
#         conn.send(msg.encode('utf8'))
#     except Exception:
#         sel.unregister(conn)
#
# def accept(sock,mask):
#     conn,addr=sock.accept()
#     conn.setblocking(False)
#     sel.register(conn,selectors.EVENT_READ,read)
#
# sock=socket.socket()
# ip_port=('127.0.0.1',9000)
# sock.bind(ip_port)
# sock.listen(5)
# sock.setblocking(False)
# sel.register(sock,selectors.EVENT_READ,accept)
#
# while True:
#     events=sel.select()
#     for key,mask in events:
#         func=key.data
#         func(key.fileobj,mask)


import socket,selectors

def accept(sock,mask):
    conn,addr=sock.accept()
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)

def read(conn,mask):
    try:
        msg=conn.recv(BUFSIZE)
        print(msg.decode('utf8'))
        msg=input('>>>: ').strip()
        conn.send(msg.encode('utf8'))
    except Exception:
        sel.unregister(conn)

sock=socket.socket()
ip_port=('127.0.0.1',9000)
BUFSIZE=1024

sock.bind(ip_port)
sock.listen(5)
sock.setblocking(False)

sel=selectors.DefaultSelector()
sel.register(sock,selectors.EVENT_READ,accept)

while True:
    events=sel.select()
    for key,mask in events:
        func=key.data
        func(key.fileobj,mask)