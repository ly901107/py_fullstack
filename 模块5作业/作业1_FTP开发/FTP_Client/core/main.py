#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/29

import socket,os
import json,hashlib
# from core.db_handler import make_header,recv_header,send_filedate,recv_filedate
# from core.account import account
from core.auth import authenticate
from core.db_handler import get_response
from conf import settings

STATUS_CODE  = {
    250 : "无效的CMD格式,例: {'action':'get','filename':'test.py','size':344}",
    251 : "无效的CMD",
    252 : "无效的身份验证数据",
    253 : "错误的用户名或密码",
    254 : "通过认证",
}

# def decorator(type):
#     def foo(func):
#         def foo1(*args,**kwargs):
#             if type == 'cmd':
#                 self,cmd=func(*args,**kwargs)
#                 head_dic = {'cmd': cmd}
#                 make_header(head_dic, self.sock)
#                 recv_msg = recv_header(self.sock)
#                 print(recv_msg.decode('gbk'))
#                 return head_dic,self
#         return foo1
#     return foo

class FtpClient(object):
    def __init__(self):
        print('客户端初始化ing......')
        self.user = None
        self.make_connection()

    def make_connection(self):
        '''
        建立链接
        :return:
        '''
        print('建立连接ing......')
        self.sock = socket.socket()
        self.sock.connect(('127.0.0.1',9000))

    def interaction(self):
        '''
        交互函数
        :return:
        '''

        self.user = authenticate(self.sock)
        if self.user:
            print("---Begin to interact with u...")
            self.terminal_display = "[%s]$: "%self.user
            while True:
                choice = input(self.terminal_display).strip()
                if len(choice) == 0:continue
                cmd_list = choice.split()
                if hasattr(self, 'client_%s'%cmd_list[0]):
                    func = getattr(self, 'client_%s'%cmd_list[0])
                    func(cmd_list)
                else:
                    print('输入有误，请重新输入或输入"help"查看帮助')

    def client_pwd(self, *args, **kwargs):
        '''
        查看所在目录
        :param args:
        :param kwargs:
        :return:
        '''
        data = {'action': 'pwd'}
        self.sock.send(json.dumps(data).encode())
        response = get_response(self.sock)
        has_err = False

        if response.get('status_code') == 200:  #任务完成
            data = response.get('data')
            if data:
                print(data)
            else:
                has_err = True
        else:
            has_err = True

        if has_err:
            print('出现错误！')

    def client_ls(self, *args, **kwargs):
        '''
        查看目录下文件
        :return:
        '''
        data = {'action':'ls'}
        self.sock.send(json.dumps(data).encode())
        response = get_response(self.sock)
        has_err = False

        if response.get('status_code') == 200:
            data =response.get('data')
            if data:
                print(data[1])
            else:
                has_err = True
        else:
            has_err = True

        if has_err:
            print('出现错误!')

    def client_cd(self, *args, **kwargs):
        '''
        切换目录
        :return:
        '''
        if len(args[0]) > 1:
            path = args[0][1]
        else:
            path = ''

        data = {'action': 'cd', 'path': path}
        self.sock.send(json.dumps(data).encode())
        response = get_response(self.sock)
        if response.get('status_code') == 260:
            self.terminal_display = "[%s]$: "% response.get('data').get('current_path')

    def client_put(self, cmd_list):
        '''
        上传文件
        :return:
        '''
        print('cmd_list', cmd_list)
        file_abs_path = '%s/%s' % (settings.UPLOAD_DIR, cmd_list[1])
        file_basename = cmd_list[1]
        print(file_abs_path)

        if len(cmd_list) == 1 or  not os.path.isfile(file_abs_path):        #判断文件是否存在
            print('文件路径不存在')
            return

        file_size= os.path.getsize(file_abs_path)
        data_header = {
            'action':'put',
            'filename':file_basename,
            'filesize':file_size
        }

        #检测是否需要进行md5检验
        if self.client_md5(cmd_list):
            data_header['md5'] = True

        self.sock.send(json.dumps(data_header).encode())        #发送报头
        response = get_response(self.sock)                      #等待回复
        print('response', response)

        if response['status_code'] == 261:

            file_obj = open(file_abs_path, 'rb')
            if self.client_md5(cmd_list):
                md5_obj = hashlib.md5()
                progress = self.show_progress(file_size)
                progress.__next__()

                for line in file_obj:
                    print('line', line, len(line))
                    self.sock.send(line)
                    md5_obj.update(line)
                    for line in file_obj:
                        self.sock.send(line)
                        try:
                            progress.send(len(line))
                        except StopIteration as e:
                            print('100%')
                else:
                    file_obj.close()
                    print('文件%s发送完成' % file_basename)
                    md5_value = md5_obj.hexdigest()
                    md5_from_server = get_response(self.sock)

                    if md5_from_server['status_code'] == 258:
                        # print('md5_from_server',md5_from_server)
                        if md5_from_server['data']['md5'] == md5_value:
                            print('文件 %s 一致性校验成功' % file_basename)
            else:
                progress = self.show_progress(file_size)
                progress.__next__()
                for line in file_obj:
                    self.sock.send(line)
                    try:
                        progress.send(len(line))
                    except StopIteration as e:
                        print('100%')
                else:
                    file_obj.close()
                    print('文件%s发送完成' % file_basename)

    def client_get(self, cmd_list):
        '''
        下载文件
        :return:
        # '''
        print('cmd_list', cmd_list)
        if len(cmd_list) == 1:
            print('文件路径不存在')
            return

        data_header = {
            'action':'get',
            'filename':cmd_list[1]
        }

        #检测是否需要进行md5检验
        if self.client_md5(cmd_list):
            data_header['md5'] = True

        self.sock.send(json.dumps(data_header).encode())        #发送报头
        response = get_response(self.sock)                      #等待回复
        print(response)

        if response['status_code'] == 257:
            self.sock.send(b'1')                            #发送确认信息

            file_basename = cmd_list[1]                     #获取文件名，用以保存
            print('file_basename',file_basename)

            recive_size = 0
            file_obj = open('%s/%s'% (settings.DOWNLOAD_DIR, file_basename), 'wb')

            if response['data']['filesize'] == 0:
                file_obj.close()
                return

            if self.client_md5(cmd_list):
                md5_obj = hashlib.md5()
                progress = self.show_progress(response['data']['filesize'])
                progress.__next__()

                while recive_size < response['data']['filesize']:
                    data = self.sock.recv(1024)
                    recive_size += len(data)
                    try:
                        progress.send(len(data))
                    except StopIteration as e:
                        print('100%')
                    file_obj.write(data)
                    md5_obj.update(data)
                else:
                    file_obj.close()
                    print('文件%s接收完成' % file_basename)
                    md5_value = md5_obj.hexdigest()
                    md5_from_server = get_response(self.sock)
                    if md5_from_server['status_code'] == 258:
                        # print('md5_from_server',md5_from_server)
                        if md5_from_server['data']['md5'] == md5_value:
                            print('文件 %s 一致性校验成功' % file_basename)
            else:
                progress = self.show_progress(response['data']['filesize'])
                progress.__next__()

                while recive_size < response['data']['filesize']:
                    data = self.sock.recv(1024)
                    recive_size += len(data)
                    try:
                        progress.send(len(data))
                    except StopIteration as e:
                        print('100%')
                    file_obj.write(data)
                else:
                    file_obj.close()
                    print('文件%s接收完成' % file_basename)

    def show_progress(self, total):
        recive_size = 0
        current_percent = 0

        while recive_size < total:
            if int(recive_size / total * 100) > current_percent:
                print('#', end= '', flush= True )
                current_percent = int(recive_size / total * 100)
            new_size = yield
            recive_size += new_size

    def client_md5(self,cmd_list):
        '''
        是否需要MD5验证
        :param cmd_list:
        :return:
        '''
        if '--md5' in cmd_list:
            return True

    def client_help(self, *args, **kwargs):
        '''
        帮助文档
        :return:
        '''
        supported_actions="""
        get filename    #从服务器下载文件
        put filename    #上传文件至服务器
        ls              #查看当前服务器目录中的文件列表
        pwd             #查看当前服务器目录中的路径
        cd path         #更改目录，与linux cd命令相同
        """
        print(supported_actions)

def main_run():
    '''
    主函数
    :return:
    '''
    ftpclient=FtpClient()
    ftpclient.interaction()

if __name__ == '__main__':
    main_run()