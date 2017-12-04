#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/28

'''
以时间戳准为创建ID
'''

import hashlib
import time

def create_id():
    m=hashlib.md5()
    m.update(str(time.time()).encode('utf-8'))
    return m.hexdigest()

