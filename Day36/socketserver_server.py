#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/27

import socketserver

ip_port=('127.0.0.1',9000)
BUFSIZE=1024

class FTPserver(socketserver.BaseRequestHandler):   #通信循环
    def handle(self):
        print(self.request)
        while True:
            try:
                date=self.request.recv(BUFSIZE)
                print(date.decode('utf8'))
                msg=input('>>>: ').strip()
                self.request.send(msg.encode('utf8'))
            except Exception:
                self.request.close


if __name__ == '__main__':
    obj=socketserver.ThreadingTCPServer(ip_port,FTPserver)
    obj.serve_forever() #链接循环