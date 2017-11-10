#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/5

from conf import settings
from core import accounts


def make_transaction(account_date,type,mount):
    mount = float(mount)
    if type in settings.TRANSACTION_TYPE:
        #计算利息
        intersets = mount * settings.TRANSACTION_TYPE[type]['interest']
        old_balabce = account_date['balance']
        if settings.TRANSACTION_TYPE[type]['action'] == 'plus':
            new_balance = old_balabce+ intersets + mount
        elif settings.TRANSACTION_TYPE[type]['action'] == 'minus':
            new_balance = old_balabce - intersets - mount
            if new_balance < 0:
                print('账户余额不足')
                return
        account_date['balance'] = new_balance
        accounts.up_current_balance(account_date)
        return account_date