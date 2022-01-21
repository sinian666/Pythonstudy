'''#、打印九九乘法表
s=[1,2,3,4,5,6,7,8,9]
n=[1,2,3,4,5,6,7,8,9]
for i in s:
    for j in n:
        a=i*j
        print(i,'*',j,'=',a,end=' ')
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+'*'+str(j)+'='+str(i*j),end='\t')
    print()