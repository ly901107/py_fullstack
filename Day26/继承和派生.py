#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/12

#每次实例化一次，计数加1
# class Garen:
#     camp = 'Demacia'
#     n = 0
#     def __init__(self,nickname,aggressivity = 54,life_value =414 ):    #英雄初始攻击力为54
#         self.nickname = nickname            #为自己的盖伦起个别名
#         self.aggressivity = aggressivity    #英雄攻击力
#         self.life_value = life_value        #英雄生命值
#         Garen.n += 1
#
#     def attack(self,enemy):                #普通攻击技能，enemy是敌人
#         enemy.life_value -= self.aggressivity  #根据自己攻击力，减少敌人的血量
#
#
# g1 = Garen('lex')
# g2 = Garen('lex')
#
# print(g1.n)     #1

#可变和不可变类型的修改

# class Garen:
#     camp = 'Demacia'
#     hobby = []
#     def __init__(self,nickname,aggressivity = 54,life_value =414 ):    #英雄初始攻击力为54
#         self.nickname = nickname            #为自己的盖伦起个别名
#         self.aggressivity = aggressivity    #英雄攻击力
#         self.life_value = life_value        #英雄生命值
#
#     def attack(self,enemy):                #普通攻击技能，enemy是敌人
#         enemy.life_value -= self.aggressivity  #根据自己攻击力，减少敌人的血量
#
#
# g1 = Garen('lex')
# g2 = Garen('alex')
#
# g1.camp = '6666'    #如果为不可变类型，修改的是对象自己的名称空间的
# print(g1.camp)      #6666
# print(g2.camp)      #Demacia
#
# g1.hobby.append('g1 hobby')     #不可变类型的修改，则还是修改的原内存地址对应的
# g2.hobby.append('g2 hobby')
# print(g1.hobby)     #['g1 hobby', 'g2 hobby']
# print(g2.hobby)     #['g1 hobby', 'g2 hobby']


# class ParentClass1:     #定义父类
#     pass
#
# class ParentClass2:     #定义父类
#     pass
#
# class SubClass1(ParentClass1):                  #单继承，基类是ParentClass1，派生类是SubClass1
#     pass
#
# class SubClass2(ParentClass1,ParentClass2):     #python支持多继承，用逗号分隔开多个继承的类
#     pass
#
# print(ParentClass1.__bases__)     #(<class 'object'>,)
# print(SubClass1.__bases__)        #(<class '__main__.ParentClass1'>,)
# print(SubClass2.__bases__)        #(<class '__main__.ParentClass1'>, <class '__main__.ParentClass2'>)


class Aniaml:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def walk(self):
        print('%s is wakling'% self.name)
    def say(self):
        print('%s is saying'% self.name)

class People(Aniaml):
    pass

# p1 = People('lex',18)
# p1.walk()
# People.walk(People,'lex',18)
# print(p1)
# print(p1.name)      #lex
# print(p1.age)       #27
# p1.walk()           #lex is wakling
#
# class Teacher:
#     def __init__(self,name,sex,course):
#         self.name = name
#         self.sex = sex
#         self.course = course
#
# class Student:
#     def __init__(self,name,sex,course):
#         self.name = name
#         self.sex = sex
#         self.course = course
#
# class Course:
#     def __init__(self,name,price,peroid):
#         self.name = name
#         self.price = price
#         self.peroid = peroid
#
# t1 = Teacher('egon','male',Course('python',15800,'7m'))
# s1 = Student('lex','male',Course('python',15800,'7m'))
# print(t1.course)        #<__main__.Course object at 0x00000000027BE4A8>
# print(s1.course.name)   #python
#
# python_obj = Course('python',15800,'7m')
# t1 = Teacher('egon','male',python_obj)
# s1 = Student('lex','male',python_obj)
# print(t1.course)        #<__main__.Course object at 0x00000000027BE710>
# print(s1.course.name)   #python


