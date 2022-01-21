#for循环
for i in range(1,6):
    print(i)
#输出10次hello
for i in range(1,11):
    print('hellow')
#输出1-100间的偶数
for i in range(1,101):
    if i%2==0:
         print(i)
#求1+2+3+4+5的和
a=0
for i in range(1,6):
    a=a+i
print(a)

for i in range(10): #起点默认是0，终点是10
    print(i)
for i in range(1,10,3): #循环变量每次加3
    print(i)
for i in range(10,1,-2): #循环变量每次减2
    print(i)