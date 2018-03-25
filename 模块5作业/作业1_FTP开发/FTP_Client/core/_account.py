#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/29

from core.auth import auth
from core.db_handler import make_header

def account(conn):
    '''
    客户端账户函数
    :param conn: 线程
    :return: 认证成功返回Ture
    '''
    while True:
        username = input('请输入账号: ').strip()
        passwd = input('请输入密码: ').strip()
        res = auth(username, passwd, conn)
        print('=======',res)
        '''
        100:服务端账户不存在
        102:服务端账户存在，密码错误
        103:服务端账户存在，认证成功
        '''
        if res['status'] == 100:
            flag=True
            while flag:
                choice = input('用户不存在，是否创建 Y/N?: ').strip()
                if not choice:continue
                #创建用户
                if choice == 'Y':
                    dic = {'status': 101}
                    make_header(dic, conn)
                    flag = False
                    continue
                elif choice == 'N':
                    flag=False
                    continue
                else:
                    print('输入有误，请重新输入')
                    continue
        elif res['status'] == 102:
            print('账号密码错误，请重新输入！')
            continue
        elif res['status'] == 103:
            print('登陆成功')
            return True
            break