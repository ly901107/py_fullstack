#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/14

#新式类继承，在查找属性时遵循：广度优先

# class A(object):
#     def test(self):
#         print('from A')
#
# class B(A):
#     def test(self):
#         print('from B')
#
# class C(A):
#     def test(self):
#         print('from C')
#
# class D(B):
#     def test(self):
#         print('from D')
#
# class E(C):
#     def test(self):
#         print('from E')
#
# class F(D,E):
#     def test(self):
#         print('from F')
#
#
# f1 = F()
# f1.test()
# #广度优先：F-->D-->B-->E-->C-->A-->object
# print(F.mro())      #[<class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.E'>,
#                         # <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# class People:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def attack(self,enemy):                 #普通攻击技能，enemy是敌人
#         enemy.life_value -= self.aggressivity   #根据自己攻击力，减少敌人的血量
#
# class Chinses(People):
#     country = 'China'
#     def __init__(self,name,age,sex,language = 'Chinese'):
#         super().__init__(name,age,sex)
#         # People.__init__(self,name,age,sex)
#         self.language = language
#
# c1 = Chinses('lex',15,'male')
# print(c1.name)
# print(c1.__dict__)
# p1 = People('lex',15,'male')
# print(p1.__dict__)


#经典类

class A:
    def test(self):
        print('from A')

class B(A):
    def test(self):
        print('from B')


class C(A):
    def test(self):
        print('from C')


class D(B):
    def test(self):
        print('from D')


class E(C):
    def test(self):
        print('from E')


class F(D, E):
    def test(self):
        print('from F')


f1 = F()
f1.test()
print(F.__mro__)
# 深度优先：F-->D-->B-->A-->E-->C-->object
