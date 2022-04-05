#!/usr/bin/env/ python3 
# -*- coding:UTF-8 -*-
# @Time      :2022/4/5 6:14 PM
# @Author    :Si Nian
# @Software  :PyCharm
#dicty与set
#字典的使用
# 举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：
#
# names = ['Michael', 'Bob', 'Tracy']
# scores = [95, 75, 85]
# 给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，list越长，耗时越长。
#
# 如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用Python写一个dict如下：
#
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
#dict 的数据存储方式为'key-value'的存储方式。
# 给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。
# 除去上述在初始化中进行定义的方法，dict 的另一种储存方式是直接通过key放入。
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
# 例如：
d['Adam'] = 67  # 在字典d里面放入一个值为'Adam'，key为67的数据。
print(d)
d['Adam'] = 57
print(d)
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Thomas' in d)
# 是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Thomas'))
print(d.get('Thomas',-1))#意思是可以设置如果这个值不存在的话可以返回的内容。
print(d)
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
print(d.pop('Bob'))
print(d)
# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
# 和list比较，dict有以下几个特点：
# 1、查找和插入的速度极快，不会随着key的增加而变慢；
# 2、需要占用大量的内存，内存浪费多。
# 而list相反：
# 1、查找和插入的时间随着元素的增加而增加；
# 2、占用空间小，浪费内存很少。
# 综上所述：dict是一种用空间换时间的方法
#dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：




