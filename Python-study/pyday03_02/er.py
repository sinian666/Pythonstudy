#2、输入节假日的名称(元旦或清明或五一或端午放假3天，十一放假7天)，
# 将输入的假日名称传递给函数，在函数中根据假日对应输出放假的天数
def sn():
    a = input("请输入节日：")
    if a == "元旦" or a == "清明节" or a == "劳动节" or a == "端午节":
        print('放假3天')
    elif a == "国庆节":
        print('放假7天')
    else:
        print("不放假，想啥呢!")
sn()