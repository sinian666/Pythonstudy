#列表
ns=[39,9.8,'abcde',True,200]
print(ns)#声明列表即查看列表。结果：[39, 9.8, 'abcde', True, 200]
print(ns[2])#查看下标为2的数据。结果：abcde
print(ns[-2])#从右到左查看下标为-2的数据。结果：True
print(ns[1:3])#查看下标为1到3的数据。结果：[9.8, 'abcde']

ns.append(800)# 追加 在列表的最后增加数据
print(ns)#(结果为：[39, 9.8, 'abcde', True, 200, 800])
ns.insert(3,'hello')#插入,3表示插入的数据的下标
print(ns)#(结果为：[39, 9.8, 'abcde', 'hello', True, 200, 800])
ns[2]=506#修改,表示修改下标为2的数据
print(ns)#(结果为：[39, 9.8, 506, 'hello', True, 200, 800])
del ns[5]#删除:删除下标为5的数据
print(ns)#(结果为：[39, 9.8, 506, 'hello', True, 800])

