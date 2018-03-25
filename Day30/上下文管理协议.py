#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/22

# class Open:
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('with中代码块执行完毕时执行我啊')
#
#
# with Open('a.txt') as f:
#     print('=====>执行代码块')
#     print(f,f.name)


class Open:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('with中代码块执行完毕时执行我啊')
        print(exc_type)
        print(exc_val)
        print(exc_tb)


with Open('a.txt') as f:
    print('=====>执行代码块')
    raise AttributeError('***着火啦,救火啊***')
print('0' * 100)  # ------------------------------->不会执行