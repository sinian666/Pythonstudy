#!/usr/bin/env/ python3 
# -*- coding:UTF-8 -*-
# @Time      :2022/4/3 8:10 PM
# @Author    :Si Nian
# @Software  :PyCharm
#循环
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9,10]:
    sum = sum + x
print(sum)
#Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
print(list(range(5)))
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for i in range(3):
    print('Hello,',L[i],'!')


#break
#在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

#continue
#在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

