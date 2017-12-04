#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/29/029
'''
登陆、注册时认证
数据认证
'''
import os

from .db_handle import Base
from conf import settings
from lib import common


class Auth(Base):
    DB_PATH = settings.ACCOUNT_PATH
    def __init__(self):
        self.id = common.create_id()

    @classmethod
    def get_obj_by_datename(cls,date):
        '''
        根据用户(数据)名获取相应的数据，如果存在返回数据
        :param date: 数据名
        :return: 认证实例化对象auth
        '''
        auths = (cls.get_obj_by_id(id) for id in os.listdir(cls.DB_PATH))
        for auth in auths:
            if auth.name == date:               #获取对象中的name与传入名称进行比较
                return auth