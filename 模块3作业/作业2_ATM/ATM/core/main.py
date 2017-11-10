#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/4


import os
from core import auth
from core import accounts
from core import transaction
from core import manage


#默认用户数据，所有用户数据的交互，需从此模块入
user_date = {
    'user_id': None,
    'authentication':False,
    'user_date':None,
    'type':'general'
}

def account_information(user_date):
    '''
    普通用户:账户信息
    :param user_date:
    :return:
    '''
    account_date = accounts.load_current_balance(user_date['user_id'])
    print(account_date)

def repay(user_date):
    '''
    普通用户:还款
    :param user_date:
    :return:
    '''
    account_date = accounts.w(user_date['user_id'])
    current_balance= ''' --------- 账户余额信息 --------
信用额度 :%s
剩余额度:%s''' %(account_date['credit'],account_date['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_mount = input('请输入还款金额: ').strip()
        if repay_mount.isdigit() and len(repay_mount):
            new_balance = transaction.make_transaction(account_date,'repay',repay_mount)
            if new_balance:
                print('账户新余额为%s'%(new_balance['balance']))

        if repay_mount == 'b':
            back_flag = True
            continue

def borrow(user_date):
    '''
    普通用户:借现
    :param user_date:
    :return:
    '''
    account_date = accounts.load_current_balance(user_date['user_id'])
    current_balance= ''' --------- 账户余额信息 --------
信用额度 :%s
剩余额度:%s''' %(account_date['credit'],account_date['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_mount = input('请输入借款金额: ').strip()
        if withdraw_mount.isdigit() and len(withdraw_mount):
            new_balance = transaction.make_transaction(account_date,'withdraw',withdraw_mount)
            if new_balance:
                print('账户新余额为%s'%(new_balance['balance']))

        if withdraw_mount == 'b':
            back_flag = True
            continue

def transfer_accounts(user_date):
    '''
    普通用户:转账
    :param user_date:
    :return:
    '''
    account_date = accounts.load_current_balance(user_date['user_id'])
    current_balance= ''' --------- 账户余额信息 --------
信用额度 :%s
剩余额度:%s''' %(account_date['credit'],account_date['balance'])
    print(current_balance)
    transfer_account = input('请输入转账账户: ').strip()
    transfer_account_date = accounts.load_current_balance(transfer_account)
    if transfer_account_date:
        back_flag = False
        while not back_flag:
            transfer_mount = input('请输入转账金额: ').strip()
            if transfer_mount.isdigit() and len(transfer_mount):
                new_balance = transaction.make_transaction(account_date,'transfer',transfer_mount)
                if new_balance:
                    print('账户新余额为%s'%(new_balance['balance']))
                    transaction.make_transaction(transfer_account_date,'repay',transfer_mount)
            if transfer_mount == 'b':
                back_flag = True
                continue

def bill(user_date):
    '''
    普通用户:查看账单
    :param user_date:
    :return:
    '''
    pass
    #TODO 未实现

def exit_program(user_date):
    '''
    普通/管理用户:退出
    :param user_date:
    :return:
    '''
    global exit_flag
    exit_flag = True

def add_account(user_date):
    '''
    管理用户:添加账户
    :param user_date:
    :return:
    '''
    back_flag = False
    while not back_flag:
        account =  input('请输入要创建的卡号: ').strip()
        manage_date = manage.account_add(account)
        if manage_date:
            print('账号%s创建成功' % account)
            back_flag = True
        if account == 'b':
            back_flag = True
            continue

def adjust_account(user_date):
    '''
    管理用户:额度调整
    :param user_date:
    :return:
    '''
    back_flag = False
    while not back_flag:
        account = input('请输入您要调整的账户: ').strip()
        credit = input('请输入您要调整的额度: ').strip()
        manage_adjust_date = accounts.load_current_balance(account)
        if manage_adjust_date:
            date = manage.account_adjust(manage_adjust_date,'adjust',credit= credit)
            if date:
                print('调整成功！')
                back_flag = True
        if account or credit == 'b':
            back_flag = True
            continue

def lock_account(user_date):
    '''
    管理用户:冻结账户
    :param user_date:
    :return:
    '''
    back_flag = False
    while not back_flag:
        account = input('请输入您要锁定的账户: ').strip()
        manage_adjust_date = accounts.load_current_balance(account)
        if manage_adjust_date:
            date = manage.account_adjust(manage_adjust_date,'lock')
            if date:
                print('锁定成功！')
                back_flag = True
        if account  == 'b':
            back_flag = True
            continue

def unlock_account(user_date):
    '''
    管理用户:解锁账户
    :param user_date:
    :return:
    '''
    back_flag = False
    while not back_flag:
        account = input('请输入您要解锁的账户: ').strip()
        manage_adjust_date = accounts.load_current_balance(account)
        if manage_adjust_date:
            date = manage.account_adjust(manage_adjust_date,'unlock')
            if date:
                print('解锁成功！')
                back_flag = True
        if account == 'b':
            back_flag = True
            continue

menu_user=u'''
------- 万里长城永不倒银行 ---------
1.  账户信息
2.  还款
3.  借现
4.  转账
5.  查看账单
6.  退出
    '''

menu_user_dic = {
'1':account_information,
'2':repay,
'3':borrow,
'4':transfer_accounts,
'5':bill,
'6':exit_program,
}

menu_admin = u'''
------- 万里长城永不倒银行 ---------
1.  添加账户
2.  额度调整
3.  冻结账户
4.  解锁账户
5.  退出
    '''

menu_admin_dic = {
'1':add_account,
'2':adjust_account,
'3':lock_account,
'4':unlock_account,
'5':exit_program,
}


def init(user_date):
    def init1(func):
        def init2(*args,**kwargs):
            if user_date['type'] == 'general':
                global menu_dic,menu
                menu_dic = menu_user_dic
                menu = menu_user
                res = func(*args,**kwargs)
                return res
            else:
                menu_dic = menu_admin_dic
                menu = menu_admin
                res = func(*args,**kwargs)
                return res
        return init2
    return init1


@init(user_date)
def interface(user_date):
    '''
    主界面交互程序
    :param user_date:
    :return:
    '''
    global exit_flag
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_choice = input('请输入数字键选择服务: ').strip()
        if user_choice in menu_dic:
            menu_dic[user_choice](user_date)


def atm_run():
    '''
    主程序运行
    :return:
    '''
    #加载认证模块，认证成功后返回用户数据
    account_date = auth.account_login(user_date)
    #认证成功，运行菜单模块
    if user_date['authentication'] == True:
        user_date['user_date'] = account_date
        # if user_date['type'] == 'general':
        interface(user_date)
