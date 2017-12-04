#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/24

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s-%(message)s-%(filename)s',
                    datefmt='%Y-%m-%d %X',
                    filename='a.log',
                    filemode='w')

logging.debug('from debug')
logging.info('from info')
logging.warning('from warning')
logging.error('from error')
logging.critical('from critical')




# L = logging.getLogger()
#
# fh = logging.FileHandler('a.log')
# sh = logging.StreamHandler()
#
# format1 = logging.Formatter('%(asctime)s-%(message)s')
#
# fh.setFormatter(format1)
# sh.setFormatter(format1)
# fh.setLevel(20)
#
# L.addHandler(fh)
# L.addHandler(sh)
# L.setLevel(10)

# logging.debug('from debug')
# logging.info('from info')
# logging.warning('from warning')
# logging.error('from error')
# logging.critical('from critical')