#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/18


# Process 类的调用
#
import time
# import random
from multiprocessing import Process

def piao(name):
    print('%s piaoing'% name)
    time.sleep(2)
    print('%s piao end'% name)


if __name__ == '__main__':

    p1 = Process(target=piao, args=('egon',))
    p2 = Process(target=piao, args=('alex',))
    p3 = Process(target=piao, args=('wupeiqi',))
    p4 = Process(target=piao, args=('yuanhao',))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    print('主线程')

# 主线程
# egon piaoing
# wupeiqi piaoing
# alex piaoing
# yuanhao piaoing
# egon piao end
# alex piao end
# wupeiqi piao end
# yuanhao piao end

# 继承Process类调用
#
# import time
# from multiprocessing import Process
#
# class piao(Process):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#     def run(self):
#         print('%s piaoing'%self.name)
#         time.sleep(2)
#         print('%s piao end'%self.name)
#
# if __name__ == '__main__':
#
#     p1=piao('egon')
#     p2=piao('alex')
#     p3=piao('wupeiqi')
#     p4=piao('yuanhao')
#
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#
#     print('主线程')

# 主线程
# egon piaoing
# alex piaoing
# yuanhao piaoing
# wupeiqi piaoing
# egon piao end
# alex piao end
# yuanhao piao end
# wupeiqi piao end

from multiprocessing import Process

global n
n=100

def foo():
    n=200
    print('子程序',n)

if __name__ == '__main__':
    p1=Process(target=foo)
    p1.start()
    print('主程序',n)

# 主程序 100
# 子程序 200