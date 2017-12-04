#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/18

# import math
# class Circle:
#     def __init__(self,radius): #圆的半径radius
#         self.radius=radius
#
#     @property
#     def area(self):
#         return math.pi * self.radius**2 #计算面积
#
#     @property
#     def perimeter(self):
#         return 2*math.pi*self.radius #计算周长
#
# c=Circle(10)
# '''
# 输出结果:
# 314.1592653589793
# 62.83185307179586
# '''
# # print(c.radius)
# # print(c.area())
# # print(c.perimeter())
# print(c.radius)
# print(c.area)
# print(c.perimeter)

# class Foo:
#     def __init__(self,val):
#         self.__NAME=val #将所有的数据属性都隐藏起来
#
#     @property
#     def name(self):
# w        return self.__NAME #obj.name访问的是self.__NAME(这也是真实值的存放位置)
#
#     @name.setter
#     def name(self,value):
#         if not isinstance(value,str):  #在设定值之前进行类型检查
#             raise TypeError('%s must be str' %value)
#         self.__NAME=value #通过类型检查后,将值value存放到真实的位置self.__NAME
#
#     @name.deleter
#     def name(self):
#         del self.__NAME
#
# f=Foo('egon')
# print(f.name)
# # f.name=10 #抛出异常'TypeError: 10 must be str'
# del f.name
# print(f.name)   #'Foo' object has no attribute '_Foo__NAME'


class People:
    def __init__(self,name,SEX):
        self.name = name
        self.sex = SEX          #设置sex 会调用property下的setter

    @property
    def sex(self):
        print('from property')
        return self.__sex

    @sex.setter
    def sex(self,value):
        print('from setter')
        self.__sex = value

    @sex.deleter
    def sex(self):
        print('from deleter')
        del self.__sex

p1 = People('Lex','male')       #from setter
#
# print(p1.__dict__)              #{'name': 'Lex', '_People__sex': 'male'}
# print(p1.sex)                   #from property
#                                 #male
# del p1.sex                      #from deleter
# print(p1.__dict__)              #{'name': 'Lex'}
