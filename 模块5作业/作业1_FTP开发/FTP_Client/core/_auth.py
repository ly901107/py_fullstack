#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/29

from core.db_handler import make_header,recv_header

def auth(username,passwd,conn):
    '''
    与服务端交互认证函数，处理认证时数据
    :param username: 用户账户
    :param passwd: 用户密码
    :param conn: 线程
    :return: 认证信息
    '''
    head_dic={'action':'auth',
        'username':username,
        'passwd':passwd}
    make_header(head_dic,conn)
    recv_msg = recv_header(conn)
    return recv_msg