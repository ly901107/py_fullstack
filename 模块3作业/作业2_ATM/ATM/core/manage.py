#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/8

from core import db_handler
from core import accounts

def account_add(account):
    '''
    管理模式增加账户
    :param account: 增加账户ID
    :return:
    '''
    db_api=db_handler.db_create
    '获取最新的用户数据'
    data = db_api("creat * from accounts where account=%s" % account)
    if data:
        print('已创建账户%s' % account)
        return True

def account_adjust(account_date,type,**kwargs):
    '''
    管理模式：调整额度、锁定、解锁账户
    :param account_date:
    :param type: 调整类型:额度调整、锁定账户、解锁账户
    :param kwargs: 调整额度
    :return:
    '''
    if type == 'adjust':
        print(kwargs)
        credit = int(kwargs.get('credit'))

        account_date['credit'] = credit
        date = accounts.up_current_balance(account_date)
        return date
    elif type == 'lock':
        account_date['status'] = 1
        date = accounts.up_current_balance(account_date)
        return date
    elif type == 'unlock':
        account_date['status'] = 0
        date = accounts.up_current_balance(account_date)
        return date
