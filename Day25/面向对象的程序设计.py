#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/11

#应用场景
#找不到共同特征和技能不用强求

#对象：学校----->归类
    #共有的特征：商标为etiantian
    #共有的技能：招生
    #独有的特征：地址不一样，老师们，课程

class School:
    tag = 'etiantian'

    def __init__(self,addr):
        self.addr = addr
        self.teacher_list = []
        self.course_list = []

    def zhaosheng(self):
        pass

#对象：老师----->归类
    #共有的技能：教课
    #独有的特征：名字，性别，level，课程
class Teacher:
    def __init__(self,name,sex,level):
        self.name = name
        self.sex = sex
        self.level = level
        self.course_list = []

    def teach(self):
        pass

#对象：学生----->归类
    #共同的特征：
    #共同的技能：search_score,hanin
    #独有的特征：学号，名字，性别，课程
class Student:
    def __init__(self,ID,name,sex,):
        self.id = ID
        self.name = name
        self.sex = sex
        self.course_list = []

    def search_score(self):
        pass

    def hanin(self):
        pass

class Course:       #将课程归类
    def __init__(self,name,price,period):
        self.name = name
        self.price = price
        self.period = period

s1 = Student('12345','lex','female')

python_obj = Course('python',15800,'7m')
linux_obj = Course('Linux',19800,'2m')

s1.course_list.append(python_obj)
s1.course_list.append(linux_obj)

print('''student name is:%s
        course name is:%s
        course price is :%s
        '''%(s1.name,s1.course_list[0].name,s1.course_list[0].price))
