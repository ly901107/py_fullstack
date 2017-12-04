#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/14

#老师、学生与课程
#老师、学生与生日
#学生与分数

class Teacher:
    def __init__(self,name,course,birthday):
        self.name = name
        self.course = course
        self.birthday = birthday

class Student:
    def __init__(self,name,course,birthday,score):
        self.name = name
        self.course = course
        self.birthday = birthday
        self.score = score

class Course:
    def __init__(self,name):
        self.name = name

class Birthday:
    def __init__(self,date):
        self.date = date

class Score:
    def __init__(self,grade):
        self.grade = grade

Course_obj = Course('python')
Birthday_obj = Birthday('2012-12-12')
Score_obj = Score(100)

s1 = Student('lex',Course_obj,Birthday_obj,Score_obj)
print(s1.course.name)
print(s1.birthday.date)
print(s1.score.grade)


