#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/29
import json
from core import main

def get_auth_result(username, passwd, conn):
    '''
    获取账号密码验证结果
    :param username: 用户名
    :param passwd: 用户密码
    :param conn: 线程
    :return:
    '''
    data = {
        'action':'auth',
        'username':username,
        'passwd':passwd
    }
    conn.send(json.dumps(data).encode())
    response=get_response(conn)
    print('response', response)

    if response.get('status_code') == 254:
        print('通过验证！')
        ftpclient = main.FtpClient()
        ftpclient.user = username
        return True
    else:
        print(response.get('status_msg'))

def get_response(conn):
    '''
    得到服务器端回复结果
    :return:
    '''
    data = conn.recv(1024)
    # print('date',date)
    data = json.loads(data.decode())
    return data