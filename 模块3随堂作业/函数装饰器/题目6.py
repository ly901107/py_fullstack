#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/30

#编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果

#

import requests

def geturl(url):
	return requests.get(url).text

g=geturl('http://www.baidu.com')
print(g)