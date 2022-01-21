'''10、输入一个整数，
判断这个数是否是一个水仙花数'''
a=int(input("输入一个整数："))
b=int(a/100)
c=int((a-b*100)/10)
d=int(a-b*100-c*10)
if a>999 and a<100:
    print(a,"不是水仙花数。")
elif a==b*b*b+c*c*c+d*d*d:
    print(a,"是水仙花数。")
else:
    print(a, "不是水仙花数。")