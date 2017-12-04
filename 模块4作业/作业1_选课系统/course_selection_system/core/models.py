#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/1

from lib import common
from conf import settings
from .auth import Auth

def decorator(index):
    '''
    创建装饰器
    Teacher，Feedback_record 存在特殊情况
    :param index: 创建类型
    :return: 返回输入值，主要是根据评价内容扣钱使用
    '''
    def _deco(func):
        def _func(cls):
            print('----------')
            back_back_flag = True
            while back_back_flag:
                back_flag = True
                record_flag = False
                b_flag = False
                while back_flag:
                    inputs=func(cls)
                    auth_record = cls.get_obj_by_datename(inputs[0])  # 获取课程数据
                    obj_cereat = cls(*inputs)
                    if 'b' in inputs:
                        b_flag = True  # 输入b跳出第一层循环
                        break
                    elif all(list(inputs)):
                        record_flag = True  # 输入内容不为空跳出第一层循环
                        break
                    else:
                        print('输入不能为空')

                if b_flag:
                    back_back_flag = False  # 输入b 跳出第二层循环
                    continue
                if record_flag:  # 当输入内容不为空时，进行课程覆盖或
                    if auth_record:  # 已经创建过
                        if index == 'Feedback_record':  #一个名字只能评价一次
                            print('您已评价一次，不能多次评价')
                            break
                        else:
                            choice = input('数据已存在,是否覆盖 Y/N? ').strip()
                            if choice == 'N':
                                continue
                            if choice == 'Y':
                                cls.remove(auth_record.id)
                                obj_cereat = cls(*inputs)
                                obj_cereat.save()
                                print('更新成功')
                    else:
                        obj_cereat.save()
                        if index == 'Teacher':          #创建老师的同时会将登陆账密创建
                            obj_register = Account(inputs[0], inputs[1], 'teacher')
                            obj_register.save()
                            print('注册成功')
                        print('创建成功')
                return inputs
        return _func
    return _deco


class Student(Auth):
    '''
    学生类
    '''
    DB_PATH = settings.STUDENT_PATH
    def __init__(self,name,passwd,age):
        '''
        :param id: 根据创建时间创造ID
        '''
        self.id = common.create_id()
        self.name = name
        self.passwd = passwd
        self.age = age


class Course_selection(Auth):
    '''
    选课列表
    '''
    DB_PATH = settings.COURSE_SELECTION_PATH
    def __init__(self,student_name,class_name):
        self.id = common.create_id()
        self.name = student_name
        self.class_name = class_name


class Class_register(Auth):
    '''
    上课记录
    '''
    DB_PATH = settings.CLASS_REGISTER_PATH
    def __init__(self,class_name,student_name,teacher_name,class_part,class_hour):
        self.id = common.create_id()
        self.name = class_name
        self.student_name = student_name
        self.teacher_name = teacher_name
        self.class_part = class_part
        self.class_hour = class_hour

    @classmethod
    @decorator('Class_register')
    def creat_class_register(cls):
        '''
        创建上课记录
        :return:
        '''
        print('欢迎来到创建上课记录模块: '.center(20, '='))
        name = input('请输入课程名或"b"退出: ').strip()
        student_name = input('请输入授课老师姓名或"b"退出: ').strip()
        teacher_name = input('请输入上课学生姓名或"b"退出: ').strip()
        class_part = input('请输入课程节次或"b"退出: ').strip()
        class_hour = input('请输入上课日期或"b"退出: ').strip()
        return name, student_name, teacher_name, class_part, class_hour

from .account import Account            #此处防止与account模块交叉导入


class Teacher(Auth):
    '''
    老师类
    '''
    DB_PATH = settings.TEACHER_PATH
    def __init__(self,name,passwd,sex,age,money):
        self.id = common.create_id()
        self.name = name
        self.passwd = passwd
        self.sex = sex
        self.age = age
        self.money = money

    @classmethod
    @decorator('Teacher')
    def cereat_teacher(cls):
        '''
        创建\更新老师信息
        :return:
        '''

        print('欢迎来到创建老师模块: '.center(20, '='))
        name = input('请输入老师名或"b"退出: ').strip()
        passwd = input('请输入密码或"b"退出: ').strip()
        sex = input('请输入老师性别或"b"退出: ').strip()
        age = input('请输入老师年龄或"b"退出: ').strip()
        money = input('请输入老师资产或"b"退出: ').strip()
        return name, passwd, sex, age, money


class Feedback_record(Auth):
    '''
    评价记录
    '''
    DB_PATH = settings.FEEDBACK_RECORD_PATH
    def __init__(self, student_name, teacher_name, evaluate):
        self.id = common.create_id()
        self.name = student_name
        self.teacher_name = teacher_name
        self.evaluate = evaluate

    @classmethod
    @decorator('Feedback_record')
    def creat_feedback(cls):
        '''
        创建评价记录
        :return:
        '''

        print('欢迎来到评价老师模块: '.center(20, '='))
        user_name = input('请输入您的名字或"b"退出: ').strip()
        teacher_name = input('请输入老师名字或"b"退出: ').strip()
        feedback = input('请输入评价(good/bad)或"b"退出: ').strip()
        return user_name, teacher_name, feedback

    @classmethod
    def increase_reduce_teacher_money(cls,feedbacks):
        '''
        根据评价记录增加、减少老师的钱
        :param feedbacks:
        :return:
        '''
        auth_record_teacher = Teacher.get_obj_by_datename(feedbacks[1])  # 获取老师数据
        if feedbacks[2] == 'good':
            print(auth_record_teacher.__dict__)
            auth_record_teacher.money = int(auth_record_teacher.money) + 100
            print('老师增加100元')
        else:
            auth_record_teacher.money = int(auth_record_teacher.money) - 100
            print('老师减少100元')

        Teacher.remove(auth_record_teacher.id)
        obj_cereat_teacher = Teacher(auth_record_teacher.name,
                                     auth_record_teacher.passwd,
                                     auth_record_teacher.sex,
                                     auth_record_teacher.age,
                                     auth_record_teacher.money)
        obj_cereat_teacher.save()


class Course(Auth):
    '''
    课程类
    '''
    DB_PATH = settings.COURSE_PATH
    def __init__(self,name,time,cprice,teacher_name):
        self.id = common.create_id()
        self.name = name
        self.time = time
        self.cprice = cprice
        self.teacher_name = teacher_name

    @classmethod
    @decorator('Course')
    def cereat_course(cls):
        '''
        创建课程
        :return:
        '''

        print('欢迎来到创建课程模块: '.center(20, '='))
        name = input('请输入课程名或"b"退出: ').strip()
        time = input('请输入上课时间或"b"退出: ').strip()
        price = input('请输入课程价格或"b"退出: ').strip()
        teacher_name = input('请输入授课老师或"b"退出: ').strip()
        return name, time, price, teacher_name


class Admin(Auth):
    '''
    管理员
    '''
    def __init__(self,name,passwd):
        self.name = name
        self.passwd = passwd

    @classmethod
    def creat_admin(cls):
        '''
        创建管理员
        :return:
        '''
        while True:
            name = input('请输入管理员账号: ').strip()
            passwd = input('请输入密码: ').strip()
            if all([name, passwd]):
                break
            else:
                print('输入不能为空')

        obj_register = Account(name, passwd, 'admin')
        obj_register.save()
        print('注册成功')