#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/14

# class Animal:
#     def run(self):
#         raise AttributeError('子类必须实现这个方法')
#
#     def speak(self):
#         raise AttributeError('子类必须实现这个方法')
#
# class People(Animal):
#     # def run(self):
#     #     print('人在跑')
#
#     # def speak(self):
#     #     print('人在说话')
#     pass
#
# Peo1 = People()
#
# Peo1.run()      #AttributeError: 子类必须实现这个方法
# Peo1.speak()

import abc

# class Animal(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def run(self):
#         pass
#     @abc.abstractmethod
#     def speak(self):
#         pass
#
# class People(Animal):
#     # def run(self):
#     #     pass
#     #
#     # def speak(self):
#     #     pass
#     pass
#
# Peo1 = People()     #TypeError: Can't instantiate abstract class People with abstract methods run, speak