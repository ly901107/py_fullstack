#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/30

'''
账户模块
学生注册功能
登陆功能
'''

from .db_handle import Base
from conf import settings
from lib import common
from .auth import Auth
from .models import Student


class Account(Base):
    '''
    账户类
    '''
    DB_PATH = settings.ACCOUNT_PATH
    def __init__(self,username,passwd,account_type):
        '''
        :param name:
        :param passwd:
        :param account_type: 账户类型
        '''
        self.id = common.create_id()
        self.name = username
        self.passwd = passwd
        self.account_type = account_type

    @classmethod
    def register(cls,account_type):
        '''
        学生账户注册
        :return:
        '''
        while True:
            username = input('请输入您的用户名: ').strip()
            passwd = input('请输入您的密码: ').  strip()
            age = input('请输入您的年龄: ').strip()
            auth_record = Auth.get_obj_by_datename(username)
            if auth_record:
                print('账号已存在')
                continue
            elif all([username, passwd, age]):
                break
            else:
                print('输入不能为空')
        obj_register = Account(username,passwd,account_type)
        obj_register.save()                                 #注册信息保存
        obj_creat_student = Student(username,passwd,age)
        obj_creat_student.save()                            #学生信息保存
        print('注册成功')
        auth_record = Auth.get_obj_by_datename(username)
        return auth_record

    @classmethod
    def login(cls):
        '''
        账户登陆
        :return:
        '''
        while True:
            name = input('请输入您的账号: ').strip()
            passwd = input('请输入您的密码: ').strip()
            auth_record = Auth.get_obj_by_datename(name)        #通过用户明获取信息
            if not auth_record or auth_record.passwd != passwd:
                print('账号密码错误，请重新输入!')
                continue
            if all([name, passwd]):
                break
            else:
                print('账号密码不得为空')
        print('登陆成功,账号类型为%s' % auth_record.account_type)
        return auth_record