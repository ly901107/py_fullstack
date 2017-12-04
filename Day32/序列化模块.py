#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/24

import json

d = {'lex':6666}

date = json.dumps(d)

# f = open('a.txt','w')
# f.write(date)
# f.close()


f = open('a.txt')
date2 = json.loads(f.read())
print(date2['lex'])