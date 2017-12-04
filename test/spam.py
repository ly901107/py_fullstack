#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/2

# #spam.py
# print('from the spam.py')
#
# money=1000
#
# def read1():
#     print('spam模块：',money)
#
# def read2():
#     print('spam模块')
#     read1()
#
# def change():
#     global money
#     money=0


# class OldboyStudent:
#     school='oldboy'
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def learn(self):
#         print('%s is learning' %self.name) #新增self.name
#
#     def eat(self):
#         print('%s is eating' %self.name)
#
#     def sleep(self):
#         print('%s is sleeping' %self.name)
#
#
# s1=OldboyStudent('李坦克','男',18)
# s2=OldboyStudent('王大炮','女',38)
# s3=OldboyStudent('牛榴弹','男',78)
# print(s1.learn)

# class Open:
#     def __init__(self,name):
#         self.name=name
#
#     def __enter__(self):
#         print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('with中代码块执行完毕时执行我啊')
#
#
# with Open('a.txt') as f:
#     print('=====>执行代码块')
#     print(f,f.name)


# class Open:
#     def __init__(self,name):
#         self.name=name
#
#     def __enter__(self):
#         print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('with中代码块执行完毕时执行我啊')
#         print(exc_type)
#         print(exc_val)
#         print(exc_tb)
#
#
#
# with Open('a.txt') as f:
#     print('=====>执行代码块')
#     raise AttributeError('***着火啦,救火啊***')
# print('0'*100) #------------------------------->不会执行

# 出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量
# =====>执行代码块
# with中代码块执行完毕时执行我啊
# <class 'AttributeError'>
# ***着火啦,救火啊***
# <traceback object at 0x00000000027ACB48>

# class Open:
#     def __init__(self,name):
#         self.name=name
#
#     def __enter__(self):
#         print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('with中代码块执行完毕时执行我啊')
#         print(exc_type)
#         print(exc_val)
#         print(exc_tb)
#         return True
#
#
#
# with Open('a.txt') as f:
#     print('=====>执行代码块')
#     raise AttributeError('***着火啦,救火啊***')
# print('0'*100) #------------------------------->会执行
#
# # 出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量
# # =====>执行代码块
# # with中代码块执行完毕时执行我啊
# # <class 'AttributeError'>
# # ***着火啦,救火啊***
# # <traceback object at 0x00000000027DCB48>
# # 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000


# def auth2(auth_type):
#     print('777777777')
#     def auth(func):
#         print('6666666666666')
#         def foo(*args, **kwargs):
#             print('888888888')
#             name = input('username: ').strip()
#             passwd = input('passwd:')
#             if auth_type == 'sql':
#                 if name == 'liuyang' and passwd == '123':
#                     print('auth successful')
#                     res = func(*args, **kwargs)
#                     return res
#                 else:
#                     print('auth error')
#             else:
#                 print('还没学会')
#
#         return foo
#
#     return auth
#
#
# @auth2(auth_type='sql')  # index = auth(index)
# def index():
#     print('welcome to index page')
#
#
# index()  # foo()
#
# class foo:
#     def __init__(self,a):
#         self.a = 1111
#         print('from foo')
#
#     def foo2(self):
#         print('from foo2')
#
#     @classmethod
#     def foo1(cls):
#         print('from foo1')
#
# f = foo.foo1()
# print(f.a)


#
# subject = {
#     'type': None,
#     'comment': None,
#     'choice': [],
#     'res': set()
# }


# res = input('>>>>: ').strip()
# # if res == None:
# #     print()
#
# print([res])

# l = []
#
# a=[2,3,4].append(5)
# print(a)


def decorator(num):
    def _deco(func):
        def _func(cls,*args,**kwargs):
            print('----------')
            func(cls,*args,**kwargs)
            print(num)
            print('===========')
        return _func
    return _deco


class Class_register():
    def __init__(self,class_name,student_name,teacher_name,class_part,class_hour):
        self.name = class_name
        self.student_name = student_name
        self.teacher_name = teacher_name
        self.class_part = class_part
        self.class_hour = class_hour


    @classmethod
    @decorator('10')
    def creat_class_register(cls,name):
        print('from creat_class_register')
        print(name)

Class_register.creat_class_register('lex')