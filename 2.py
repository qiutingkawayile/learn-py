#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python 编码问题
# 由于 Python的诞生比Unicode标准发布的时间还要早 早期 python 只支持ASCII编码 普通字符串在 python 中是 ASCII编码

# 字母与数字对应转换
print 'A is', ord('A')
print '65 is', chr(65)

# 后来 python 添加了对 Unicode 的支持
# 以u''来定义以 Unicode 编码的字符串
print u'滚犊子'

# Unicode 编码转 utf-8
print u'哈哈哈'.encode('utf-8')

# 用 len 函数求字符串的长度
# 英文字符转换后表示的UTF-8的值和Unicode值相等（值相等）
print len('12312')
# 中文字符转换后1个Unicode字符将变为3个UTF-8字符
print len('呀呀呀') == 9
