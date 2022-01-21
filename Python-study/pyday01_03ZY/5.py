'''5、从键盘输入两个数字，再输入一个
运算符号(+或-或*或/),然后根据运算符进行运算'''
a=int(input("第一个数字："))
b=int(input("第二个数字："))
c=input("运算符号：")
if c=="+":
    d=a+b
    print(d)
elif c=="-":
    d=a-b
    print(d)
elif c=="*":
    d=a*b
    print(d)
elif c=="/":
    d=a/b
    print(d)
else:
    print("运算符号输入错误，无法运算。")