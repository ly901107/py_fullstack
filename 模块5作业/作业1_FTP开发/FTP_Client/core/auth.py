#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/29
from core.db_handler import get_auth_result

def authenticate(conn):
    '''
    账号密码验证函数
    :param conn: 线程
    :return:
    '''
    retry_count = 0
    while retry_count < 3:
        username = input('username: ').strip()
        passwd = input('passwd: ').strip()
        if get_auth_result(username, passwd, conn):
            return username
        retry_count += 1
