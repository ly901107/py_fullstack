#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/31

#将names=['egon','alex_sb','wupeiqi','yuanhao']中以sb结尾的名字过滤掉，然后保存剩下的名字长度

names=['egon','alex_sb','wupeiqi','yuanhao']
names=[len(name) for name in names if not name.endswith('sb')]
print(names)