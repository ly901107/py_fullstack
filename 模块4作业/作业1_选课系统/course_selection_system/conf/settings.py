#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/30/030

'''
数据文件路径设置
'''

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ACCOUNT_PATH = os.path.join(BASE_DIR,'db','accounts')
CLASS_REGISTER_PATH = os.path.join(BASE_DIR,'db','class_register')
COURSE_PATH = os.path.join(BASE_DIR,'db','course')
COURSE_SELECTION_PATH = os.path.join(BASE_DIR,'db','course_selection')
FEEDBACK_RECORD_PATH = os.path.join(BASE_DIR,'db','feedback_record')
STUDENT_PATH = os.path.join(BASE_DIR,'db','student')
TEACHER_PATH = os.path.join(BASE_DIR,'db','teacher')