#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/27

import socket
import json
import struct

class FtpClient:
    def __init__(self):
        self.sock=socket.socket()

    def connect(self,ip_port):
        self.sock.connect(ip_port)

    def run(self):
        while True:
            msg=input('>>>: ').strip()
            if not msg:continue
            msg_l=msg.split()
            cmd=msg_l[0]
            if hasattr(self,cmd):
                func=getattr(self,cmd)
                func(cmd)

    def ls(self,*args):
        cmd=args[0]
        if cmd == 'ls':
            head_dic={'cmd':cmd}

            #指定报头
            head_json=json.dumps(head_dic)
            head_json_bytes=bytes(head_json,encoding='utf8')
            head_struct=struct.pack('i',len(head_json_bytes))

            #发送报头和数据
            self.sock.send(head_struct)
            self.sock.send(head_json_bytes)
            #接收报头
            date=self.sock.recv(4)
            date_size=struct.unpack('i',date)
            print(date_size)
            date_size=date_size[0]

            #接收数据
            recv_msg=b''
            recv_size=0
            while recv_size < date_size:
                date=self.sock.recv(date_size)
                recv_size += len(date)
                recv_msg += date
            print(recv_msg.decode('gbk'))

if __name__ == '__main__':
    ftpclient=FtpClient()
    ftpclient.connect(('127.0.0.1',9000))
    ftpclient.run()