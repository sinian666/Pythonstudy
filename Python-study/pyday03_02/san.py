#3、声明一个函数，参数是起点、终点，返回起点到终点之间所有15的倍数的和,输入起点和终点，调用函数。
def sn():
    a=int(input('请输入起点：'))
    b=int(input('请输入终点：'))
    s=0
    for i in range(a,b):
        if i%15==0:
            s+=i
    return s
c=sn()
print(c)

