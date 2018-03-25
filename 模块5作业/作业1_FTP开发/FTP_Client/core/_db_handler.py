#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/29

import json
import struct

def make_header(head_dic,conn):
    print(type(head_dic))
    print(head_dic)
    head_json = json.dumps(head_dic)
    print(head_json)
    head_json_bytes = bytes(head_json, encoding='utf8')
    head_struct = struct.pack('i', len(head_json_bytes))
    return send_header(head_struct,head_json_bytes,conn)

def send_header(head_struct,head_json_bytes,conn):
    conn.send(head_struct)
    print('head_struct',head_struct)
    conn.send(head_json_bytes)
    print('head_json_bytes', head_json_bytes)

def send_filedate(filename,conn):
    send_size=0
    with open(filename,'r') as f:
        for line in f:
            conn.send(line)
            send_size += len(line)
            print(send_size)
        else:
            print('send successful')

def recv_header(conn,code='utf8',json_flag=True):
    '''
    接收报头数据大小
    :param conn: 线程
    :param code: 解码格式
    :return:
    '''
    print('========',code,json_flag)
    date=conn.recv(4)
    date_size=struct.unpack('i',date)[0]
    return recv_date(date_size,conn,code='utf8',json_flag=True)

def recv_date(date_size,conn,code='utf8',json_flag=True):
    '''
    接收报头数据
    :param date_size:报头大小
    :param conn:线程
    :param code:编码格式
    :param json_flag:是否需要json反序列化
    :return:接收到的报头数据
    '''
    recv_msg=b''
    recv_size=0
    while recv_size < date_size:
        date=conn.recv(1024)
        recv_size += len(date)
        recv_msg += date
    recv_msg = recv_msg.decode(code)
    if json_flag:
        recv_msg = json.loads(recv_msg)
    return recv_msg

def recv_filedate(filename,filedate_size,conn):
    recv_msg=b''
    recv_size=0
    while recv_size < filedate_size:
        with open(filename,'w') as f:
            date=conn.recv(1024)
            recv_size += len(date)
            recv_msg += date
            f.write(recv_msg.decode('utf8'))
    else:
        print('下载完成')