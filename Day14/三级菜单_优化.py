#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/10/4

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

present_choice = menu
last_choice = [menu]

while True:
	for key in present_choice:		#打印出列表
		print(key)
	choice = input(">:")		#等待输入
	if len(choice) == 0:
		continue
	if choice in present_choice:
		last_choicepresent_choice.append(present_choice)		#将现在这一层 增加到列表中
		 = present_choice[choice]

	if choice == 'b':
		if last_choice:
			present_choice = last_choice[-1]
			last_choice.pop()
	if choice == 'q':
		break