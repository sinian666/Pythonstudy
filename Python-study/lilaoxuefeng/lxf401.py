# -*- coding:UTF-8 -*-
# @Time      :2022/4/1 10:31 PM
# @Author    :Si Nian
# @Software  :PyCharm
#!/usr/bin/env/ python3   添加这一行注释是为了让自己的代码能子啊命令行中运行起来。
# Unicode编码：单个的提供两个函数
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(chr(66))
print(ord('中'))#ValueError: chr() arg not in range(256)爆出这种错误是因为在python2中chr( n) 将编码n 转为字符，n的范围是 0 ~ 255
# 而python 3.0中，chr(n) 将编码n 转为字符，n的范围是 0 ~ 65535
print(chr(25991))

print('\u4e2d\u6587')#用16进制写等同

#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
#Python对bytes类型的数据用带b前缀的单引号或双引号表示：  x = b'ABC'
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

#纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，
# 因为中文编码的范围超过了ASCII编码的范围，Python会报错。
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。
# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：

print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))


#格式化字符串的3种方式：
#输出类似'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串，而xxx的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方式。
#1、d% 替换内容为整数、s% 替换内容为字符串  f%  替换内容为浮点数   x% 替换内容为16进制的整数
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

#2、format()
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

#3、f-string：最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')#.后面的数字便是保留小数点以后的几位数
#结果： The area of a circle with radius 2.5 is 19.62

s1 = 72
s2 = 85
r = (s2-s1)/72*100
print(f'小明成绩提升的百分点是：{r:.1f}%')#错误原因没有加'.'
print('小明成绩提升的百分点是：{0:.1f}%'.format(r))



#使用list与tuple

sn =['1','2','3','4','5']#list是一个可变有序表，，表里面的数据类型也可以不同，甚至是另外一个list。
#计算list长度
print(len(sn))
#索引定位元素
print(sn[1])#正数，从0开始
print(sn[-1])#获取倒数第一个元素；-4即倒数第四个

#追加元素到末尾
sn.append('6')
print(sn)
#中间插入元素
sn.insert(1,'1.5')
print(sn)
#定位删除某个元素(要删除的元素处于末尾时候不需要添加索引！)
sn.pop(1)
print(sn)
#直接将某个元素替换成另一个元素
sn[5]='7'
print(sn)

# 表里面的数据类型也可以不同，甚至是另外一个list。
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
print(s[2][1])#想要去'php'的话；

#列表为空的话，它的长度是0

#tuple：元组，他与list的不同在于元组里面的内容是不可以进行更改的，没有添加，插入、删除等等操作，可以靠索引定位。
sy=(1,2,3,4)
print(sy[1])
#只有一个元素的元组在定义时需要在元素后面加上'，'
ss=(1,)#这只一个元组

#也有可变的元组：表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
# tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

#练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])


#条件判断：if、elif、else
#练习：小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
height = 1.75
weight = 80.5
bim=weight/(height*height)
if bim <18.5:
    print('过轻')
elif bim>=18.5 and bim<25:
    print("正常")
elif bim>=25 and bim<28:
    print("过重")
elif bim>=28 and bim<32:
    print("肥胖")
else:
    print("严重肥胖")

#完成练习过程中，忘记了if、elif、else后面要加的是冒号":"

