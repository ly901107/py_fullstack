#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/31

# class Garen:
#     camp = 'Demacia'
#
#     def __init__(self,nickname):
#         self.nick = nickname    #g1.nick = '草丛伦'
#
#     def attack(self):
#         print('=======>',self.nick)     #g1.nick
#         print('attack')
#
# print(Garen)	#<class '__main__.Garen'>
# g1 = Garen('草丛伦')       #Garen.__init__(g1,'草丛伦')
# g2 = Garen('猥琐伦')
#
# #Garen.attack()  #调用的是函数,报错
# g1.attack()     #绑定函数调用，会自动传参，self = g1
#


# class Garen:
#     camp = 'Demacia'
#
#     def __init__(self,nickname):
#         self.nick = nickname    #g1.nick = '草丛伦'
#
#     def attack(self):
#         print('=======>',self.nick)     #g1.nick
#         print('attack')
#
# # print(Garen)        #查
# # Garen.camp = 'aaaa' #改
# # del Garen.camp      #删
# # Garen.x = 1         #增
#
# #
# g1 = Garen('alex')
# Garen.attack(g1)

# print(g1.nick)      #查
# g1.attack()
# g1.nick = 'asb'     #改
# del g1.nick         #改
# g1.sex = 'female'   #增

class Student:
    country = 'China'
    def __init__(self,ID,NAME,SEX,PROVINCE):
        self.id = ID
        self.name = NAME
        self.sex = SEX
        self.province = PROVINCE

    def search_score(self):
        print('tell score')

s1 = Student('12345','alex','female','shandong')        #实例化，没有返回值，返回为none

print(Student.country )        #类的变量引用
print(Student.__init__)        #类的函数引用
print(Student.search_score)    #类的函数引用