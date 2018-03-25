#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/23

import hashlib
# #
# # m = hashlib.md5()
# # m.update('alex'.encode('utf-8'))
# # print(m.hexdigest())
#
# print('%s%%' %(100))
#
# print('[%-2s]' %'#')
# print('[%15s]' %'#')
# print(('[%%-%ds]' %50) %'#')

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf8'))
md5.update('python hashlib?'.encode('utf8'))
print(md5.hexdigest())

md5.update('how to use md5 in python hashlib?'.encode('utf8'))
print(md5.hexdigest())