#5、输入一个字符串，计算这个字符串中a字母的个数和b字母的个数
s='avafanciavabbnda'
c=0
d=0
for i in s:
    if i=='a':
        c+=1
    elif i=='b':
        d+=1
print('a字母的个数是',c)
print('b字母的个数是',d)