#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/29

import json

STATUS_CODE  = {
    200:"任务完成",
    250:"无效的CMD格式,例: {'action':'get','filename':'test.py','size':344}",
    251:"无效的cmd",
    252:"无效的验证数据",
    253:"错误的用户名或密码",
    254:"通过身份验证",
    255:"文件名没有提供",
    256:"服务器上不存在文件",
    257:"准备好发送文件",
    258:"md5验证",
    259:"在服务器上不存在路径",
    260:"路径改变",
    261:"准备好接收文件",
    262: "上传文件已超最大磁盘容量",
}

def send_response(conn, status_code, data=None):
    '''
    向客户端返回数据
    :param conn:
    :param status_code:
    :param date:
    :return:
    '''
    response = {
        'status_code':status_code,
        'status_msg':STATUS_CODE[status_code]
    }

    if data:
        response.update({'data':data})

    conn.send(json.dumps(response).encode())
