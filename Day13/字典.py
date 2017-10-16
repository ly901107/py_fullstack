#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/2

dict1 = {
		1:"iphone1",
		2:"iphone2",
		3:"iphone3",
		4:"iphone4",
		5:"iphone5",
		6:"iphone6"
}

dict2 = {
		1:"iphone10",
		2:"iphone20"
}
print(dict1[6])
print(dict1.get(110))
print(110 in dict1)
print(dict1.pop(6))
print(dict1)