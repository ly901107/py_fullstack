#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/21


#三个任务，一个接收用户输入，一个将用户输入的内容格式化成大写，一个将格式化后的结果存入文件

from threading import Thread

msg_l=[]
format_l=[]

def input_msg():
    while True:
        msg=input('>>>: ').strip()
        if not msg:continue
        msg_l.append(msg)

def format_msg():
    while True:
        if msg_l:
            res=msg_l.pop()
            format_l.append(res.upper())

def save_msg():
    while True:
        if format_l:
            res=format_l.pop()
            with open('a.txt','a',encoding='utf-8') as f:
                f.write('%s\n'%res)

if __name__ == '__main__':

    t1=Thread(target=input_msg)
    t2=Thread(target=format_msg)
    t3=Thread(target=save_msg)

    t1.start()
    t2.start()
    t3.start()

