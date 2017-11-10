#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/10

import credit

def payment(method):
    def foo(func):
        def foo2(*args,**kwargs):
            res = func(*args,**kwargs)
            print(total_cost)
            if method == 'credit' and total_cost != 0:
                credit.consume(total_cost)
            else:
                print('未消费，退出购物商城')
            return res
        return foo2
    return foo


shopping_list = [
    ["iphone7", 5800],
    ["臭豆腐", 100],
    ["甜不辣", 20],
    ["拖鞋", 50],
    ["coffee", 200]
]  # 购物清单

shopping_cart = {}

total_cost = 0

@payment('credit')
def shopping():
    global total_cost
    exit_flag = False
    while not exit_flag:
        num = 1
        print('商品信息'.center(20,'-'))
        for key in shopping_list:
            print(num,key)
            num += 1
        choice = input("请输入商品编号或按'b'退出: ").strip()
        quantity = input('请输入购买数量: ').strip()
        if choice == 'b':
            for key in shopping_cart:
                total_cost += int(shopping_cart[key][0]) * int(shopping_cart[key][1])  # 打印总花费及余额
            print(total_cost)
            print('结账ing.....')
            exit_flag = True
        if choice.isdigit() and quantity.isdigit():
            choice = int(choice)
            quantity = int(quantity)
            if choice > 0 and choice <= len(shopping_list) + 1:
                product = shopping_list[choice - 1]  # 商品列表为		product
                product_name = product[0]  # 商品名为		product[0]
                product_price = product[1]  # 商品价格为		product[1]
                cost = product_price * quantity  # 单次购买花费为	cost
                print('已加入购物车买商品%s，共计金额%s' % (product_name, cost))
                if product_name in shopping_cart:  # 商品名已存在购物车
                    shopping_cart[product_name][0] += quantity
                else:  # 商品第一次购买
                    shopping_cart[product_name] = [quantity, product_price]  # 将购买信息加入购物车

            else:
                print('输入错误，请重新输入！')
                continue


shopping()