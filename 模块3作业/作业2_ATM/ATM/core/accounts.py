#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/5
from core import db_handler

def load_current_balance(user_id):
    '''
    获取最近的用户信息
    :param user_id:
    :return: 用户信息
    '''
    db_api = db_handler.db_execute
    '获取最新的用户数据'
    data = db_api("select * from accounts where account=%s" % user_id)
    return data



def up_current_balance(account_date):
    '''
    上传用户信息
    :param account_date:
    :return:
    '''
    db_api = db_handler.db_execute
    '获取最新的用户数据'
    data = db_api("update accounts where account=%s" % account_date['id'],account_date = account_date)
    return data