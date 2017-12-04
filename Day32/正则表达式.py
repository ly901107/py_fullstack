#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/25

import re

# # print(re.findall('www.(?:baidu)|(?:oldboy).com','www.baidu.com'))
# print(re.findall("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>"))
# print(re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>").group())
# print(re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>").group())

# print(re.findall('\s','hello egon 123'))
# ret1=re.findall('李.','李爽\nalex\n李四\negon\nalvin\n李二')
# print(ret1)
# ret2=re.findall('^李.','李爽\nalex\n李四\negon\nalvin\n李二')
# print(ret2)
# ret3=re.findall('李.$','李爽\nalex\n李四\negon\nalvin\n李二')
# print(ret3)
#
# print(re.findall('ab{2,4}','abbb'))
# print(re.findall('a[1*-]b','a1b a*b a-b'))
#
# print(re.findall('a[0-9]b','a1b a*b a-b a=b'))
#
# print(re.findall(r'c\\l','abc\le'))
# print(re.findall('(?:ab)+123','ababab123'))

# print(re.findall('compan(?:y|ies)','Too many companies have gone bankrupt, and the next one is my company'))

# ret=re.findall('(ab)|\d','rabhdg8sd')

ret = re.findall('(\d{1,3}){3}\d{3}','123456123')
print(ret)

# print(re.search('w','alex make love'))