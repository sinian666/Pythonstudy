'''#循环字符串
s='vbc'
for i in range(0,len(s)):#这时候的i表示下标
    print(i)
for i in s:  #这时候的i表示每个字符
    print(i)'''

'''#声明一个字符串，统计字符串中字母a的数量
s='asdfghasdfgasdfaatghjk'
b=0
for i in s:
    if i=='a':
        b=b+1
print(b)#r如果放在和if对齐的位置，表示循环一次输出一个数字'''
#声明一个字符串，输出所有小写字母
s='xcvghCFVGBcfvg'
for i in s:
    #if i>'a'and i<'z':    #效果相同a-z也是一种顺序
        #print(i)
    if i.islower():#.islower()是一个表示小写字母的参数。可以记下来。
        print(i)
