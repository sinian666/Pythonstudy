'''9、定义个变量46，求出46是这一年的第几
周第几天
(假设1月1日是星期一)'''
a=46
b=int(a/7)+1   #也可以写成b=a//7,得到的结果直接是整数
c=int(a%7)
if a%7==0:
    b=a//7
    c=7
    print('46是这一年的第',b,'周的第',c,'天')
else:
    print('46是这一年的第',b,'周的第',c,'天')