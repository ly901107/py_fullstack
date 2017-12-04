#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/14

class People:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def attack(self,enemy):                 #普通攻击技能，enemy是敌人
        enemy.life_value -= self.aggressivity   #根据自己攻击力，减少敌人的血量

class Chinses:
    country = 'China'
    pass

# c = Chinses('lex',18,'male')

c = Chinses()
d = People('lex',12,'male')
print(c.__dict__)       #{'name': 'lex', 'age': 18, 'sex': 'male'}
print(d.__dict__)
print(c.country)        #China