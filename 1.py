#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 第一句 告诉 linux 系统该文件是一个可执行程序


print 'hello world'

print 'my name is', 'python', 'and you'

# name = raw_input('enter your name:')
# print 'your name is', name

# a = raw_input('enter one number:')
# if a > 10:
#     print a
# else:
#     print -a

print True + True
print True + False

# 与运算
print True and True
print True and False

# 或运算
print True or False
print False or False

# 非运算
print '非运算 not True :', not True

# 空值
print None

# 变量动态声明
tmp = 121
tmp = 'yes'
tmp = False


# 理解变量在内存中的创建过程
weather = 'sun'
# 1.内存先创建'sun'字符串
# 2.内存创建 weather 变量 并把它指向 'sun'

# 练习
a = 'ABC'
b = a
a = 'XYZ'
print b
# 'ABC'

# 整数除以整数 得整数
print 10 / 3

# 浮点数除以整数 得浮点数
print 10.0 / 3

# 取余
print 10 % 3


# python 把任何数据都看成一个“对象”，而变量就是在程序中用来指向这些数据对象的，对变量赋值就是把数据和变量给关联起来
