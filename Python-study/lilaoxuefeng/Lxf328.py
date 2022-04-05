# -*- coding: utf-8 -*-
# @Time      :2022/3/28 8:57 AM
# @Author    :Si Nian
# @Software  :PyCharm
#!/usr/bin/env/ python3  #添加该行注释是为了能够项运行exe文件一样运行.py文件。
print('I\'m \"OK\"!')  # 转义字符的用法，如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识
#如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义，可以自己试试：
print('\\\t\\')
print(r'\\\t\\')
#Python还允许用r''表示''内部的字符串默认不转义
print(r'''hello,\n
...world
...fuck''')
print('''line1
...line2
...line3''')#Python允许用'''...'''的格式表示多行内容
# print('Hello，world')
# print(100)
# name = input('Please enter your name:')
# print(name)
# print(type(name))