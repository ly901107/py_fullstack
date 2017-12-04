#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/11

# #定义学生类
# #特征：共同国际'China'
# # 技能：查看成绩
# # 独有特征：ID、名字、性别、省
#
# class Student:
#     country = 'China'
#     def __init__(self,ID,NAME,SEX,PROVINCE):
#         self.id = ID
#         self.name = NAME
#         self.sex = SEX
#         self.province = PROVINCE
#
#     def search_score(self):
#         print('tell score')
#
# s1 = Student('12345','alex','female','shandong')
# #Student.__init__(s1,'12345','alex','female','shandong')

# #在python3中，所有的类都是新式类
# class A:pass
# print(A.__bases__)      #(<class 'object'>,)
#
# #在python2中，新式类
# class B(object):pass
# class C(B):pass
#
# print(B.__bases__)      #(<class 'object'>,)
# print(C.__bases__)      #(<class '__main__.B'>,)
#
# #在python2中，经典类
# class D:pass
# print(D.__bases__)

#对象的交互
# class Garen:
#     camp = 'Demacia'
#
#     def __init__(self,nickname,aggressivity = 54,life_value =414 ):     #英雄初始攻击力为54
#         self.nickname = nickname            #为自己的盖伦起个别名
#         self.aggressivity = aggressivity    #英雄攻击力
#         self.life_value = life_value        #英雄生命值
#
#     def attack(self,enemy):                 #普通攻击技能，enemy是敌人
#         enemy.life_value -= self.aggressivity   #根据自己攻击力，减少敌人的血量
#
# class Riven:
#     camp = 'Noxus'
#
#     def __init__(self,nickname,aggressivity = 54,life_value =414 ):     #英雄初始攻击力为54
#         self.nickname = nickname            #为自己的瑞文起个别名
#         self.aggressivity = aggressivity    #英雄攻击力
#         self.life_value = life_value        #英雄生命值
#
#     def attack(self,enemy):                 #普通攻击技能，enemy是敌人
#         enemy.life_value -= self.aggressivity   #根据自己攻击力，减少敌人的血量
#
# r1 = Riven('瑞雯雯')
# g1 = Garen('草丛伦')
#
# print(r1.life_value)
# g1.attack(r1)
# print(r1.life_value)


# class Student:
#     country = 'China'
#     def __init__(self,ID,NAME,SEX,PROVINCE):
#         self.id = ID
#         self.name = NAME
#         self.sex = SEX
#         self.province = PROVINCE
#
#     def search_score(self):
#         print('tell score')
#
# s1 = Student('12345','alex','female','shandong')        #实例化，没有返回值，返回为none
#
# Student.search_score()

class OldboyStudent:
    school='oldboy'
    def learn(self):
        print('is learning')
    print('-------')