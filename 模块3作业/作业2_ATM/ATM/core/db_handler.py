#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/5

import os,json
from conf import settings
from db import account_sample

def db_execute(sql,**kwargs):

    '''
    从数据库读取或上传数据
    '''
    #获取配置文件
    conn_params = settings.DATABASE
    #获取数据具体存放的accounts位置
    db_path = '%s/%s' %(conn_params['path'],conn_params['name'])
    sql_list = sql.split('where')
    if sql_list[0].startswith('select') and len(sql_list)>1:
        val_l,val_r = sql_list[1].strip().split('=')
        if val_l == 'account':
            #获取用户数据路径
                account_file = '%s/%s.json'%(db_path,val_r)
                if os.path.isfile(account_file):
                    with open(account_file,'r',encoding='utf-8') as f:
                        db_date = json.load(f)
                        return db_date
                else:
                    exit('用户不存在')

    elif sql_list[0].startswith('update') and len(sql_list) > 1:
        val_l, val_r = sql_list[1].strip().split('=')
        if val_l == 'account':
        #获取用户数据路径
            account_file = '%s/%s.json' % (db_path, val_r)
            if os.path.isfile(account_file):
                account_date = kwargs.get('account_date')
                with open(account_file,'w',encoding='utf-8') as f:
                    date = json.dump(account_date,f)
                return True

def db_create(sql):
    '''
    创建新用户
    :param sql:
    :return:
    '''
    conn_params = settings.DATABASE
    #获取数据具体存放的accounts位置
    db_path = '%s/%s' %(conn_params['path'],conn_params['name'])
    sample_path = '%s/%s' %(conn_params['path'],'account_sample')
    sql_list = sql.split('where')
    if sql_list[0].startswith('creat') and len(sql_list)>1:
        val_l,val_r = sql_list[1].strip().split('=')
        if val_l == 'account':
            #获取用户数据路径
                account_file = '%s/%s.json'%(db_path,val_r)
                if os.path.isfile(account_file):
                    exit('账户已存在，无法创建')
                else:
                    account_file = '%s/%s.json' % (db_path, val_r)
                    with open(account_file, 'w', encoding='utf-8') as f:
                        date = json.dump(account_sample.account_dic, f)
                    return True