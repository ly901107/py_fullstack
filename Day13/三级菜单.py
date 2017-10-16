#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/2

# 要求:
#
# 1.打印省、市、县三级菜单
# 2.可返回上一级
# 3.可随时退出程序

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{1},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{666},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{
		'临沂':{
			'苍山':{
				'刘媛媛':{
					'刘媛媛作业写完了吗'
				}
				}
			},
		'济南':{
			'高新区':{
				'冯冰茹':{
					'冯冰茹又晒黑了吗'
				}
			}
		}
	},
}

exit_flag = False

# def function(value,choice,exit_flag):
# while not exit_flag:
# 	for key in value:		#输出列表
# 		print(key)
# 	choice = input(">:")  # 等待输入
# 	if choice == 0:			#判断输入是否为空
# 		continue
# 	if choice == "q":
# 		exit_flag = True
# 		continue
while not exit_flag:
	for key in menu:		#打印出"北京"、"上海"、"山东"
		print(key)
	choice = input(">:")		#等待输入
	if choice == 0:			#判断输入是否为空
		continue
	if choice == "q":
		exit_flag = True
		continue
	if choice in menu:		#判断输入是否在"北京、上海、山东"
		while not exit_flag:
			next_layer= menu[choice]
			for key in next_layer:
				print(key)
			choice2 = input(">>:")  # 等待输入
			if choice2 == 0:  # 判断输入是否为空
				continue
			if choice2 == "b":
				break
			if choice2 == "q":
				exit_flag = True
				continue
			if choice2 in next_layer:	#判断输入是否在"海淀昌平朝阳东城"
				while not exit_flag:
					next_layer2 = next_layer[choice2]
					for key in next_layer2:
						print(key)
					choice3 = input(">>>:")  # 等待输入
					if choice3 == 0:  # 判断输入是否为空
						continue
					if choice3 == "b":
						break
					if choice3 == "q":
						exit_flag = True
						continue
					if choice3 in next_layer2:	#判断输入是否在"县名"
						while not exit_flag:
							next_layer3 = next_layer2[choice3]
							for key in next_layer3:
								print(key)
							choice4 = input(">>>>:")  # 等待输入
							if choice4 == 0:  # 判断输入是否为空
								continue
							if choice4 == "b":
								break
							if choice4 == "q":
								exit_flag = True
								continue
							if choice4 in next_layer3:  # 判断输入是否在"单位名"
								while not exit_flag:
									next_layer4 = next_layer3[choice4]
									for key in next_layer4:
										print(key)
									choice5 = input(">>>>>:")  # 等待输入
									if choice5 == 0:  #判断输入是否为空
										continue
									if choice5 == "b":
										break
									if choice5 == "q":
										exit_flag = True
