#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2018/3/26

from conf import settings
from threading import Thread
import paramiko

def show_host_list():
    '''
    分组显示并选择 主机信息
    :return:
    '''
    for index, key in enumerate(settings.msg_dic):
        print(index + 1, key, len(settings.msg_dic[key]))       #分组序号、分组名称、分组包含信息数量
    while True:
        choose_host_list = input('请输入分组号(eg: group1): '.strip())
        host_dic = settings.msg_dic.get(choose_host_list)
        if host_dic:
            for key in host_dic:
                print(key, host_dic[key])
            return host_dic                                     #返回选择的主机信息

        else:
            print('分组不存在,请重新输入！')
            continue

def interactive(choose_host_list):
    '''
    输入操作指令
    并且根据分组中 主机数量开启线程
    :param choose_host_list:
    :return:
    '''
    thread_list = []
    while True:
        cmd = input('请输入cmd指令: ').strip()
        # print(choose_host_list)
        if cmd:
            for key in choose_host_list:
                hostname, username, passwd, port = choose_host_list[key]['IP'], \
                                                   choose_host_list[key]['username'], \
                                                   choose_host_list[key]['password'], \
                                                   choose_host_list[key]['port']

                print(hostname, username, passwd, port)
                remote_obj = Remote_host(hostname, username, passwd, port, cmd)      #实例化
                t = Thread(target= remote_obj.run)                                  #开启线程
                t.start()
                thread_list.append(t)

            for t in thread_list:
                t.join()

        else:
            print('输入有误，请重新输入！')
            continue

class Remote_host():
    '''
    远程主机
    '''
    def __init__(self, hostname, username, passwd, port, cmd):
        self.hostname = hostname
        self.username = username
        self.passwd = passwd
        self.port = port
        self.cmd = cmd

    def run(self):
        '''
        开启线程后通过cmd命令选择相应的命令方法
        :return:
        '''
        cmd_str = self.cmd.split()[0]               #分割cmd 命令
        print(cmd_str)
        if hasattr(self, cmd_str):                  #判断类中是否存在此方法
            getattr(self, cmd_str)
        else:
            setattr(self, cmd_str, self.command)    #将其他cmd命令设置为command
            getattr(self, cmd_str)()                #调用command

    def put(self):
        '''
        上传文件
        :return:
        '''
        filename = self.cmd.split()[1]
        try:
            t = paramiko.Transport((self.hostname, self.port))
            t.connect(username=self.username, password=self.passwd)
            sftp = paramiko.SFTPClient.from_transport(t)
            sftp.put(filename, filename)
            sftp.close()
        except Exception as e:
            print('链接错误！')

    def command(self):
        '''
        执行操作命令
        主要依靠于paramiko模块
        :return:
        '''
        print('from command')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.passwd)
        stdin, stdout, stderr = ssh.exec_command(self.cmd)
        print(stdout.readlines())                   #输出结果
        ssh.close()

def run():
    '''
    主函数的运行函数
    :return:
    '''
    # print('from run')
    choose_host_list = show_host_list()
    interactive(choose_host_list)


