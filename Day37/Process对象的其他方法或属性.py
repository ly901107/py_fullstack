#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/20

# from multiprocessing import Process
# import time
#
# class Piao(Process):
#
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print('%s is piaoing'% self.name)
#         time.sleep(2)
#         print('%s piao end'% self.name)
# if __name__ == '__main__':
#     p=Piao('egon')
#     p.start()
#
#     p.terminate()       #关闭进程,不会立即关闭,所以is_alive立刻查看的结果可能还是存活
#     print(p.is_alive()) #结果为Ture
#
#     time.sleep(1)
#
#     print(p.is_alive()) #结果为Flase


from multiprocessing import Process
import time

class Piao(Process):

    def __init__(self,name):
        self.name = name
        super().__init__()

    def run(self):
        print('%s is piaoing'% self.name)
        time.sleep(2)
        print('%s piao end'%self.name)

if __name__ == '__main__':

    p=Piao('egon')
    p.start()
    print('PID',p.pid)

# PID 57104
# Piao-1 is piaoing
# Piao-1 piao end