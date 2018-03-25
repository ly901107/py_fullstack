#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/7

import socket
import subprocess
import struct
import socketserver

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port = ('127.0.0.1',8080)
BUFSIZE = 1024

s.bind(ip_port)
s.listen(5)

while True:
    conn,addr = s.accept()
    while True:
        cmd = conn.recv(BUFSIZE)
        if not cmd:break
        res = subprocess.Popen(cmd.decode('utf-8'),
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

        stderr = res.stderr.read()
        stdout = res.stdout.read()

        datesize = len(stdout) + len(stderr)

        #发送报头
        conn.send(struct.pack('i',datesize))

        #发送数据
        conn.send(stderr)
        conn.send(stdout)
    conn.close()

s.close()
