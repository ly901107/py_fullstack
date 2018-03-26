#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/30
import configparser
from conf import settings


def authenticate(username, passwd, conn):
    '''
    验证用户数据
    验证成功返回用户数据
    :return:用户名、密码
    '''
    config = configparser.ConfigParser()
    config.read(settings.DB_DIR)

    if username in config.sections():
        passwd_bak = config[username]['Passwd']
        if passwd == passwd_bak:
            # print('通过验证====', username)
            config[username]['Username'] = username
            return config[username]