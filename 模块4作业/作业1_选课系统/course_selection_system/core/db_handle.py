#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/29/029

'''
数据保存/下载模块
'''

import pickle
import os

class Base:
    '''
    数据传输保存
    '''
    def save(self):
        '''
        将id作为路径进行保存
        :return:
        '''
        file_path = r'%s/%s'%(self.DB_PATH,self.id)
        print('======',file_path)
        pickle.dump(self,open(file_path,'wb'))

    @classmethod
    def get_obj_by_id(cls,id):
        '''
        类可以直接调用，通过id获取相应的信息
        :param id:
        :return:
        '''
        file_path = r'%s/%s'%(cls.DB_PATH,id)
        return pickle.load(open(file_path,'rb'))

    @classmethod
    def remove(self,id):
        '''
        类可以直接调用，通过id将对应的文件移除，覆盖操作使用
        :param id:
        :return:
        '''
        file_path = r'%s/%s'%(self.DB_PATH,id)
        os.remove(file_path)

    @classmethod
    def get_objs(cls):
        '''
        类可以直接调用
        :return: 将类路径中的所有文件列出，遍历操作时使用
        '''
        return (cls.get_obj_by_id(id) for id in os.listdir(cls.DB_PATH))
