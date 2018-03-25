#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/22
#
# # 串行执行
# import time
#
# def consumer(res):
#     '''任务1:接收数据,处理数据'''
#     pass
#
# def producer():
#     '''任务2:生产数据'''
#     res=[]
#     for i in range(10000000):
#         res.append(i)
#     return res
#
# start=time.time()
#
# # 串行执行
# res=producer()
# consumer(res)           #注意：写成consumer(producer())会降低执行效率
#
# stop=time.time()
#
# print(stop-start)       #1.455082893371582


# 基于yield并发执行
# import time
#
# def consumer():
#     '''任务1:接收数据,处理数据'''
#     while True:
#         x=yield
#
# def producer():
#     '''任务2:生产数据'''
#     g=consumer()
#     next(g)
#     for i in range(10000000):
#         g.send(i)
#
# start=time.time()
# producer()
# stop=time.time()
#
# print(stop-start)       #1.5010855197906494

