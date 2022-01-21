#1、从键盘输入两个数字,再接收一个运算符号(+或-或*或/),
#将输入的两个数字和运算符传递给函数，在函数中根据运算符对两个数字进行运算
def s():
    a=int(input('请输入第一个数字：'))
    b=int(input('请输入第一个数字：'))
    c=input('请输入运算符号：')
    n=0
    if c=='+':
        n=a+b
        print(n)
    elif c=='-':
        n=a-b
        print(n)
    elif c=='*':
        n=a*b
        print(n)
    elif c=='/':
        n=a/b
        print(n)
s()