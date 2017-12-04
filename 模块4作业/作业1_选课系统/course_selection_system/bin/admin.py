#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/3

'''
运行此模块会执行创建管理员操作
'''

import sys,os

BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import models

if __name__=='__main__':
    models.Admin.creat_admin()