'''#列表循环
ns=[39,9.8,'abcde',True,200]
for i in range(0,len(ns)):
    print(ns[i])#此时’i‘表示的是下标
for i in ns:
    print(i)#此时’i‘表示的是每个数据'''
#声明一个列表，包含10个整数，输出列表中的奇数。
s=[11,12,13,14,15,16,17,18,19,20]
for i in s:
    if i%2==1:
        print(i)#结果：11 13 15 17 19