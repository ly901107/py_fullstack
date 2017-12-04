#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/24

# import json
#
# # dic={'name':'alvin','age':23,'sex':'male'}
# dct='{"1":111}'
# # print(type(dic))
#
# j = json.loads(dct)
# print(j)
# # print(j)
# # f = open('a.json','w')
# # # f.write(j)
# # json.dump(dic,f)
# # f.close()
# #
# # f= open('a.json','r')
# # # j = f.read()
# # # print(f)
# # # date = json.loads(j)
# # date = json.load(f)
# # f.close()
# # print(date)


import pickle

dic={'name':'alvin','age':23,'sex':'male'}

print(type(dic))

# j = pickle.dumps(dic)
# print(j,type(j))

# f = open('b','wb')
# # f.write(j)
# pickle.dump(dic,f)
# f.close()

f=open('b','rb')
# j = pickle.loads(f.read())
j = pickle.load(f)
f.close()
print(j)