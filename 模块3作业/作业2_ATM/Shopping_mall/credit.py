#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/10
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR+'\\ATM')

from core import auth
from core import transaction


def consume(total_cost):
    account = input('请输入您的信用卡账号: ').strip()
    passwd = input('请输入您的行用卡密码: ').strip()
    payment_date = auth.account_auth(account, passwd)
    print('账户现有余额为%s' % (payment_date['balance']))
    if payment_date:
        new_balance = transaction.make_transaction(payment_date, 'transfer', total_cost)
        if new_balance:
            print('账户消费后余额为%s' % (new_balance['balance']))