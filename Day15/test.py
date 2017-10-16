#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/9

d = {1: "yuan", "name": "alex"}

for key,value in d.items():
	print("{key}----->{value}".format(key=key, value = value))
	print(str(key)+"---->"+ str(value))