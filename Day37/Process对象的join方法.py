#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/20


# 示例1
# import time
# from multiprocessing import Process
#
# class Piao(Process):
#
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print('%s is piaoing'%self.name)
#         time.sleep(2)
#         print('%s piao end'%self.name)
#
# if __name__ == '__main__':
#     p=Piao('egon')
#     p.start()
#     p.join(1)
#     print('主程序')



#示例2
import time
from multiprocessing import Process

def piao(name):
    print('%s piaoing'% name)
    time.sleep(3)
    print('%s piao end'% name)


if __name__ == '__main__':

    p1 = Process(target=piao, args=('egon',))
    p2 = Process(target=piao, args=('alex',))
    p3 = Process(target=piao, args=('wupeiqi',))
    p4 = Process(target=piao, args=('yuanhao',))

    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    #
    # p1.join()
    # p2.join()
    # p3.join()
    # p4.join()
    p_l=[p1, p2, p3, p4]
    for p in p_l:
        p.start()

    for p in p_l:
        p.join()


    print('主线程')