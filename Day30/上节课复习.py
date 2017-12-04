#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Lex"
# Date: 2017/11/21


# class List(list): #继承list所有的属性，也可以派生出自己新的，比如append和mid
#     def append(self, p_object):
#         ' 派生自己的append：加上类型检查'
#         if not isinstance(p_object,int):
#             raise TypeError('must be int')
#         super().append(p_object)
#
#     @property
#     def mid(self):
#         '新增自己的属性'
#         index=len(self)//2
#         return self[index]


# class List:
#     def __init__(self,item):
#         self.x = list(item)
#
#     def append(self,object):
#         if not isinstance(object,str):
#             raise TypeError('must be str')
#         self.x.append(object)
#
#     @property
#     def mid(self):
#         index = (len(self.x)//2)
#         return self.x[index]
#
#     def __getattr__(self, item):
#         res = getattr(self.x,item)
#         return res
#
# l = List([1,2,3])
# # l.mid()
# # l.append('1')
# print(l.mid)

# class List:
#     def __init__(self,x):
#         self.l = list(x)
#
#     def append(self, p_object):
#         ' 派生自己的append加上类型检查，覆盖原有的append'
#         if not isinstance(p_object,int):
#             raise TypeError('must be int')
#         self.seq.append(p_object)
#
# l=List([1,2,3])
# print(l)
# l.append(4)
# print(l)

# class Foo:
#     def test(self):
#         print('-------')
#
# f = Foo()
#
# print(getattr(Foo,'test'))
# res1 = getattr(Foo,'test')
# res1(f)
#
# print(getattr(f,'test'))
# res2 = getattr(f,'test')
# res2()

# class Foo(list):
#
#     def append(self, object):
#         if not isinstance(object,int):
#             raise TypeError('must be int')
#         super().append(object)
#
#     @property
#     def mid(self):
#         index = len(self)//2
#         return self[index]
#
# l = Foo([1,2,3])
# print(l)
# l.append(444)
# print(l)
# print(l.mid)

# class List:
#     def __init__(self,item):
#         self.seq = list(item)
#
#     def append(self,object):
#         if not isinstance(object,int):
#             raise TypeError('must be int')
#         self.seq.append(object)
#
#     @property
#     def mid(self):
#         index = len(self.seq)//2
#         return self.seq[index]
#
#     def __getattr__(self, item):
#         res = getattr(self.seq,item)
#         return res
#
#     def __str__(self):
#         return str(self.seq)
#
# l = List([1,2,3])
# print(l)
#
# l.append(5555)
# print(l)
#
# print(l.mid)


class List:
    def __init__(self,seq):
        self.seq=list(seq)

    def append(self, p_object):
        ' 派生自己的append加上类型检查，覆盖原有的append'
        if not isinstance(p_object,int):
            raise TypeError('must be int')
        self.seq.append(p_object)

    @property
    def mid(self):
        '新增自己的方法'
        index=len(self.seq)//2
        return self.seq[index]

    def __getattr__(self, item):
        return getattr(self.seq,item)

    def __str__(self):
        return str(self.seq)

l=List((1.2,3))
# l.append(444)
# print(l)
print(l.__dict__)