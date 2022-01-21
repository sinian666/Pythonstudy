#6、在函数中声明m和n两个参数，
# 函数中打印一个m*n的矩形，并计算该矩形的面积， 将其作为方法返回值。
def sn(m,n):
    for i in range(0,m):
        for i in range(0,n):
            print('*',end='')
        print()
        s=m*n
    return(s)
a=sn(6,7)
print(a)
