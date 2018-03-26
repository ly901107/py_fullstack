#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/12/28

import socketserver,json,subprocess,re,os,hashlib,configparser
from core.db_handler import send_response
from core.auth import authenticate
from conf import settings

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
    262:"上传文件已超最大磁盘容量"
}

ip_port=('127.0.0.1',9000)

class FtpServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            if not self.data:
                print('客户端关闭')
                break
            data = json.loads(self.data.decode())
            if data.get('action') is not None:
                if hasattr(self, 'server_%s'%data.get('action')):
                    func = getattr(self, 'server_%s'%data.get('action'))
                    func(data)
                else:
                    print('无效的cmd')
                    send_response(self.request, 251)
            else:
                print('无效的cmd格式')
                send_response(self.request, 250)

    def server_auth(self, *args, **kwargs):
        '''
        认证函数
        :param args:
        :param kwargs:
        :return:
        '''
        # print('from server_auth')
        data = args[0]

        if data.get('username') is None or data.get('passwd') is None:
            send_response(self.request, 252)

        user = authenticate(data.get('username'), data.get('passwd'), self.request)
        if user is None:
            send_response(self.request, 253)
        else:
            print('通过验证！', user)

            #Windows下
            # self.home_dir = '%s\\%s'%(settings.HOME_DIR, data.get('username'))

            self.home_dir = '%s/%s' % (settings.HOME_DIR, data.get('username'))
            self.current_dir = self.home_dir
            self.username = user
            send_response(self.request, 254)

    def run_cmd(self, cmd):
        '''
        运行shell命令并且返回结果
        :param cmd:
        :return:
        '''
        cmd_res = subprocess.getstatusoutput(cmd)
        return cmd_res

    def get_relative_path(self, abs_path):
        '''
        获取相对路径
        :param abs_path:
        :return:
        '''
        # print('get_relative_path')
        relative_path = abs_path.replace(settings.BASE_DIR, '')
        return relative_path

    #TODO 对用户进行磁盘配额、不同用户配额可不同
    def judge_home_size(self, file_size):
        '''
        判断上传文件是否超过目录额定大小
        :return:
        '''
        config = configparser.ConfigParser()
        config.read(settings.DB_DIR)

        home_size_bak = config[self.username]['home_size']       #获取配置文件中用户定义的目录大小
        dir_size = os.path.getsize(self.home_dir)                #当前家目录大小
        print('dir_size', dir_size)

        if (file_size + dir_size) < home_size_bak:               #判断是否超过磁盘最大限额
            return True


    def server_ls(self, *args, **kwargs):
        '''
        查看当前目录文件
        :param args:
        :param kwargs:
        :return:
        '''
        # print('from server_ls')
        #Windows下
        # res = self.run_cmd(r'dir %s' % self.current_dir)

        res = self.run_cmd(r'ls %s' % self.current_dir)
        # print('res', res)
        send_response(self.request, 200, data=res)

    def server_pwd(self, *args, **kwargs):
        '''
        查看当前服务器目录中的路径
        :param args:
        :param kwargs:
        :return:
        '''
        # print('from server_pwd')
        res = self.get_relative_path(self.current_dir)
        send_response(self.request, 200, data=res)

    def server_cd(self, *args, **kwargs):
        '''
        更改目录，与linux cd命令相同
        :param args:
        :param kwargs:
        :return:
        '''
        # print('from server_cd')

        if args[0]:
            dest_path = "%s%s" % (self.current_dir, args[0]['path'])
        else:
            dest_path = self.home_dir

        real_path = os.path.realpath(dest_path)

        if real_path.startswith(self.home_dir):
            if os.path.isdir(real_path):
                self.current_dir = real_path
                current_relative_dir = self.get_relative_path(self.current_dir)
                res = {'current_path': current_relative_dir}
                send_response(self.request, 260 ,data = res)
            else:
                send_response(self.request, 259)
        else:
            print('路径没有权限', real_path)
            current_relative_dir = self.get_relative_path(self.current_dir)
            res = {'current_path': current_relative_dir}
            send_response(self.request, 260, data=res)

    def server_put(self, *args, **kwargs):
        '''
        上传文件至服务器
        :param args:
        :param kwargs:
        :return:
        '''
        # print('from server_put')
        # print('args',args)
        # print('kwargs', kwargs)
        data = args[0]
        # print('data', data)
        if data.get('filename') == None:
            send_response(self.request, 255)

        file_abs_path = '%s/%s' % (self.current_dir, data.get('filename'))
        # print('file_abs_path',file_abs_path)
        file_obj = open(file_abs_path, 'wb')
        file_base_name = data['filename']
        file_size = data['filesize']
        # TODO 增加判断是否超过磁盘最大容量
        if not self.judge_home_size(file_size):
            send_response(self.request, 262)
            return
        # print('file_size', file_size)
        send_response(self.request, 261)

        if data.get('md5'):                     #判断是否需要MD5校验
            md5_obj = hashlib.md5()
            recive_size = 0
            while recive_size < file_size:
                data = self.request.recv(1024)
                recive_size += len(data)
                file_obj.write(data)
                md5_obj.update(data)
            else:
                file_obj.close()
                md5_value = md5_obj.hexdigest()
                data = {'md5': md5_value}
                send_response(self.request, 258, data)
                print('文件%s接收完成' % file_base_name)
        else:
            recive_size = 0
            while recive_size < file_size:
                data = self.request.recv(1024)
                recive_size += len(data)
                file_obj.write(data)
            else:
                file_obj.close()
                print('文件%s接收完成' % file_base_name)

    def server_get(self, *args, **kwargs):
        '''
        从服务器下载文件
        :param args:
        :param kwargs:
        :return:
        '''
        # print('from server_get')
        # print('args',args)
        # print('kwargs', kwargs)
        data = args[0]
        # print('data', data)
        if data.get('filename') == None:
            send_response(self.request, 255)

        file_abs_path = '%s/%s'%(self.current_dir, data.get('filename'))
        # print(file_abs_path)

        if os.path.isfile(file_abs_path):
            file_obj = open(file_abs_path,'rb')
            file_size = os.path.getsize(file_abs_path)
            send_response(self.request, 257, data = {'filesize':file_size})
            self.request.recv(1)

            if data.get('md5'):
                md5_obj = hashlib.md5()
                for line in file_obj:
                    self.request.send(line)
                    md5_obj.update(line)
                else:
                    file_obj.close()
                    md5_value = md5_obj.hexdigest()
                    data = {'md5': md5_value}
                    send_response(self.request, 258, data)
                    print('文件%s发送完成' % data['filename'])
            else:
                for line in file_obj:
                    self.request.send(line)
                else:
                    file_obj.close()
                    print('文件%s发送完成' % data['filename'])

        else:
            send_response(self.request, 256)

def main_run():
    ftpserver = socketserver.ThreadingTCPServer(ip_port,FtpServer)
    ftpserver.serve_forever()

if __name__ == '__main__':
    main_run()
