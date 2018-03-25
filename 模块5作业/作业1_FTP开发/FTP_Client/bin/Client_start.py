#! /usr/bin/env python
# -*- coding: utf-8 -*-send_response(self.request, 260
# __author__ = "Lex"
# Date: 2017/12/28

import sys,os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
# print(sys.path)


from core import main

if __name__ == '__main__':
    main.main_run()
