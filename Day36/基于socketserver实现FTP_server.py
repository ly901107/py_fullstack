#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/27

import socketserver
import json
import struct
import subprocess

ip_port=('127.0.0.1',9000)

class FtpServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            date=self.request.recv(4)
            print('date',date)
            date_size=struct.unpack('i',date)[0]
            head_json=self.request.recv(date_size).decode('utf-8')
            head_dic=json.loads(head_json)
            cmd=head_dic['action']
            if hasattr(self,cmd):
                func=getattr(self,cmd)
                func(head_dic)

    def ls(self,*args):
        head_dic = args[0]
        if head_dic['action'] == 'ls':
            res=subprocess.Popen('dir',shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            stderr=res.stderr.read()
            stdout=res.stdout.read()

            #报头长度
            datesize=len(stdout)+len(stderr)
            date_size_struct=struct.pack('i',datesize)
            #发送报头
            self.request.send(date_size_struct)

            self.request.send(stderr)
            self.request.send(stdout)

    def auth(self,*args):
        head_dic = args[0]
        if head_dic['action'] == 'auth':
            username=head_dic['username']
            passwd=head_dic['passwd']

            datesize=len(username)+len(passwd)
            date_size_struct=struct.pack('i',datesize)

            self.request.send(date_size_struct)

            username=json.dumps(username).encode('utf-8')
            passwd=json.dumps(passwd).encode('utf-8')


            self.request.send(username)
            self.request.send(passwd)


if __name__ == '__main__':
    ftpserver=socketserver.ThreadingTCPServer(ip_port,FtpServer)
    ftpserver.serve_forever()