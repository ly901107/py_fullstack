#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/30

import sys

from .models import Course_selection,Class_register,Teacher,Feedback_record,Course
from .account import Account

main_run_dic={}
student_run_dic={}
teacher_run_dic={}
admin_run_dic={}

#保留用户登录后信息
user_date = {
    'user_name':None,
    'type':None
}

def make_route(index, dic):
    '''
    界面装饰器
    自动添加界面选项
    :param index: 选项序号
    :param dic: 选项程序名
    :return:
    '''
    def foo(func):
        dic[index]=func
    return foo

def init(num,dic):
    '''
    界面初始化
    :param num: 返回/退出序号
    :param dic: 界面选项保存字典
    :return:
    '''
    def init1(func):
        def init2(*args,**kwargs):
            exit_flag = True
            while exit_flag:
                print('欢迎来到Tesla选课系统'.center(20, '='))
                res = func(*args, **kwargs)
                choice = input('请输入要操作编号: ').strip()
                if choice == num:
                    exit_flag = False
                    continue
                if choice in dic:
                    dic[choice]()
                else:
                    print('输入有误，请重新输入')
                    continue
            return res
        return init2
    return init1

@make_route('1', student_run_dic)
def select_course():
    '''
    学生视图
    1 选课
    :return:
    '''
    course_list = []
    select_list = []
    back_flag = True
    while back_flag:
        filter_courses = Course.get_objs()      #获取所有课程信息
        course_record = Course_selection.get_obj_by_datename(user_date['user_name'])    #通过用户名获取选课列表
        num = 1                                                                         #的信息
        print('现有课程如下'.center(20,'='))
        for filter_course in filter_courses:
            print('''\n%s. %s'''%(num,filter_course.name))
            course_list.append(filter_course.name)              #打印出的课程加入到列表中
            num += 1
        choice = input('请输入课程名或b返回： ').strip()
        if choice == 'b':
            back_flag = False
            continue

        if choice in course_list:
            if course_record:                                   #选过课
                Course_selection.remove(course_record.id)       #覆盖删除
                select_list = list(course_record.class_name)    #选课列表重新赋值
            select_list.append(choice)
            select_list = set(select_list)                      #集合去重
            obj_select_course = Course_selection(user_date['user_name'], select_list)
            obj_select_course.save()                            #将新的选课信息写入
            print('选课成功')
        else:
            print('输入有误')
            continue

@make_route('2', student_run_dic)
def take_course_selection():
    '''
    学生视图
    2 查看已选课程
    :return:
    '''
    course_record = Course_selection.get_obj_by_datename(user_date['user_name'])    #通过名字获取选课信息
    # course_record = Course_selection.get_obj_by_user_defined('name',user_date['user_name'])
    num = 1
    print('已选择课程如下'.center(20,'='))
    for course in course_record.class_name:         #遍历用户出选课列表
        print('''\n%s. %s'''%(num,course))
        num += 1

@make_route('3',student_run_dic)
def check_class_record():
    '''
    学生视图
    3 查看上课记录
    :return:
    '''
    teacher_run_dic['2']()          #直接调用老师的查看上课记录 check_course_register()

@make_route('4',student_run_dic)
def feedback():
    '''
    学生视图
    4 评价老师
    :return:
    '''
    res = Feedback_record.creat_feedback()                  #调用评价类中的创建评价功能
    if res:                                                 #res=返回 评价输入的内容
        Feedback_record.increase_reduce_teacher_money(res)  #调用评价类中的增减老师钱功能

@make_route('1',teacher_run_dic)
def create_course_register():
    '''
    老师视图
    1 创建上课记录
    :return:
    '''
    # Class_register.creat_class_register()       #v1直接调用上课记录中的创建功能
    Class_register.creat_class_register()  # v2直接调用上课记录中的创建功能

@make_route('2',teacher_run_dic)
def check_course_register():
    '''
    老师视图
    2 查看上课记录
    :return:
    '''
    while True:
        choice = input('请输入您要查看的课程名或者"b"退出: ').strip()
        course_register_record = Class_register.get_obj_by_datename(choice)     #通过课程名获取课程信息
        if choice == 'b':
            break
        if not course_register_record:
            print('输入有误，请重新输入!')
            continue
        else:
            print('''%s %s %s %s %s'''
                  %(course_register_record.name,
                 course_register_record.student_name,
                 course_register_record.teacher_name,
                 course_register_record.class_part,
                 course_register_record.class_hour))

@make_route('1',admin_run_dic)
def create_course():
    '''
    管理视图
    1 创建、更新课程
    :return:
    '''
    Course.cereat_course()          #直接调用课程类中的创建功能

@make_route('2',admin_run_dic)
def create_course_register():
    '''
    管理视图、更新老师
    :return:
    '''
    Teacher.cereat_teacher()            #直接调用老师的创建功能

@init('5',student_run_dic)
def student_run():
    '''
    学生界面
    1 选课
    2 查看已选课程
    3 查看上课记录
    4 评价老师
    5 返回
    :return:
    '''
    msg='''
    1 选课
    2 查看已选课程
    3 查看上课记录
    4 评价老师
    5 返回
    '''
    print(msg)

@init('3',teacher_run_dic)
def teacher_run():
    '''
    老师界面
    1 创建上课记录
    2 查看上课记录
    3 返回
    :return:
    '''
    msg='''
    1 创建上课记录
    2 查看上课记录
    3 返回
    '''
    print(msg)

@init('3',admin_run_dic)
def admin_run():
    '''
    管理界面
    1 添加/更新课程
    2 添加/更新教师
    3 返回
    :return:
    '''
    msg='''
    1 添加/更新课程
    2 添加/更新教师
    3 返回
    '''
    print(msg)

@make_route('1',main_run_dic)
def student_register():
    '''
    学生注册
    调用账户模块的注册功能
    :return:
    '''
    account = Account.register('student')
    user_date['user_name'] = account.name           #注册后重新获取最新的用户信息
    user_date['type'] = account.account_type

@make_route('2',main_run_dic)
def login():
    '''
    账号登录
    调用账户模块的登陆功能
    登录完成后保存登录用户信息
    :return:
    '''
    account = Account.login()
    user_date['user_name'] = account.name           #登陆后重新获取最新的用户信息
    user_date['type'] = account.account_type

def main_run():
    '''
    程序主界面：
    1 学生注册
    2 账号登陆
    3 退出
    :return:
    '''
    msg = '''
    1 学生注册
    2 账号登陆
    3 退出
    '''
    while True:
        print('欢迎来到万里长城永不倒选课系统'.center(20, '='))
        print(msg)
        choice = input('请输入要操作编号: ').strip()
        if choice == '3':
            sys.exit('谢谢使用！')
        if choice in main_run_dic:
            main_run_dic[choice]()
            if user_date['type'] == 'student':      #通过用户信息中的类型判断进入哪个视图
                student_run()
            elif user_date['type'] == 'teacher':
                teacher_run()
            elif user_date['type'] == 'admin':
                admin_run()
        else:
            print('输入有误，请重新输入')
            continue

if __name__ == '__main__':
    main_run()