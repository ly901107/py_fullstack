#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/2


account = {
	"name":"刘媛媛",
	"id":12345,
	"info":[10000,0]
}
account2 = account.copy()
account2["name"] = "王俊凯"


account["info"][1] += 5000
print(account,account2)
