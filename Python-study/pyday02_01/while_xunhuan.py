
'''#while 循环
i=9
while i<10 and i>0:
    i-=1
    print(i)'''

'''#求1-100间偶数的和
i=1
while i<101:
    if i%2==0:
        print (i)
    i=i+1'''
#求1-100间偶数的和
i=1
s=0
while i<101:
    if i%2==0:
       s=s+i
    i=i+1
print(s)#【2550】