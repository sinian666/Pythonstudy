#2、输出1--100之间所有15的倍数的和
a=0
for i in range(1,101):
    if i%15==0:
        a=a+i
print(a)