#5、输入一个字符串，将输入的字符串传递给函数，
# 在函数中计算这个字符串中a字母的个数，返回a字母的个数
def sn():
    a=input('请输入一个字符串：')
    s=0
    for i in a:
        if i=='a':
            s+=1
    return (s)
b=sn()
print(b)


