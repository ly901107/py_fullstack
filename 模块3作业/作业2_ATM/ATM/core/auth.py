#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/4


from core import db_handler

def account_auth(account,passwd):
    '''
    用户认证
    :param account:
    :param passwd:
    :return:data 用户最新数据
    '''
    db_api=db_handler.db_execute
    '获取最新的用户数据'
    data = db_api("select * from accounts where account=%s" % account)
    if data['status'] == 0:
        if data['password'] == passwd:
            return data
        else:
            print('账号或密码错误，请重新输入')
    else:
        exit('账户已被锁定')

def account_login(user_date):
    '''
    用户登录模块
    :param user_date:
    :return:auth_resault 用户最近数据
    '''
    retry_count = 0
    while retry_count < 3 and user_date['authentication'] is not True:
        account = input('请输入您的卡号: ').strip()
        passwd =input('请输入您的密码: ').strip()
        '调用认证模块'
        auth_resault = account_auth(account,passwd)
        if auth_resault:
            user_date['authentication'] = True
            user_date['user_id'] = account
            if auth_resault['type'] == 'admin':
                user_date['type'] = 'admin'
            return auth_resault
        retry_count += 1
    else:
        pass
        #TODO   输出次数过多，记录报文

