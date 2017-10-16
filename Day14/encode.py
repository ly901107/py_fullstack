#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/3

name = "中国"	#utf-8格式的编码
print name
print name.decode("utf-8")		#将utf-8格式转换成Unicode格式，然后系统会自动转换成当前显示的编码
print name.decode("utf-8").encode("GBK")		##将utf-8格式转换成Unicode格式，
												##然后转换成GBK模式
gbk = name.decode("utf-8").encode("GBK")
print gbk
print gbk.decode("GBK").encode("gb2312")
name = []
name.append()