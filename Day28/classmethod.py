#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/19

# import time

# class Date:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     @staticmethod   #相当于给类扩展功能
#     def now():      #用Date.now()形式去产生实例，该实例用的是当前时间
#         t = time.localtime()    #获取结构化的时间格式
#         obj = Date(t.tm_year,t.tm_mon,t.tm_mday)    #新建实例并且返回
#         return obj
#
# class EuroDate(Date):
#     pass
#
# e1 = EuroDate.now()
# print(e1)           #<__main__.Date object at 0x0000000001E8B320>

# class foo:
#     def foo1(self):
#         pass
#
# class foo2(foo):
#     pass
#
# f1 = foo2()
# print(f1)       #<__main__.foo2 object at 0x00000000026C89B0>


# import time
# class Date:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     @classmethod
#     def now(cls):
#         t = time.localtime()    #获取结构化的时间格式
#         obj = cls(t.tm_year,t.tm_mon,t.tm_mday)    #新建实例并且返回
#         return obj
#
# class EuroDate(Date):
#     def __str__(self):
#         return '<year:%s,mont:%s,day:%s>'%(self.year,self.month,self.day)
#
# e1 = EuroDate.now()
# print(e1.__dict__)
# print(e1)           #<year:2017,mont:11,day:19>
                    #<__main__.EuroDate object at 0x00000000021FB320>

# class FOO:
#     def bar(self):
#         pass
#
#     @classmethod    #把一个方法绑定给类：类.绑定到类的方法(),会把类本身当做第一个参数自动传给绑定到类的方法
#     def test(cls,x):
#         print(cls,x)    #拿掉一个类的内存地址后，就可以实例化或者引用类的属性了
#
# f = FOO()
# print(f.bar)        #<bound method FOO.bar of <__main__.FOO object at 0x000000000269B208>>    对象的绑定方法
# print(f.test)       #<bound method FOO.test of <class '__main__.FOO'>>                        类的绑定方法
# print(FOO.test)     #<bound method FOO.test of <class '__main__.FOO'>>                        类的绑定方法
#
# f.test(111)         #<class '__main__.FOO'> 111，实例可以调用，但是传入的是实例对应的类
# FOO.test(111)       #<class '__main__.FOO'> 111


class MySQL:
    def __init__(self,host,port):
        self.host=host
        self.port=port

    @classmethod
    def from_conf(cls):
        print(123)
        return cls(1234,666)

# print(MySQL.from_conf) #<bound method MySQL.from_conf of <class '__main__.MySQL'>>
conn=MySQL.from_conf()
print(conn)
conn.from_conf() #对象也可以调用，但是默认传的第一个参数仍然是类
# print(conn.from_conf())
# conn1=MySQL()