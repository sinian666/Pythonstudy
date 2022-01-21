'''输入一个数，判断它是奇数还是偶数
a=input("请输入一个数：")
b=int(a)%2
if b==1:
    print("奇数")
elif int(a)==0:
    print("既不是奇数，也不是偶数")
else:
    print("偶数")
#输入一个生日，判断它是几零后
birth=int(input("请输入你的生日："))
if birth>=2020:
    print("你还是个20瓜娃子")
elif birth>=2010:
    print("你还是个10后的瓜娃子")
elif birth>=2000:
    print("你是一个00后的小鲜肉")
else:
    print("你出生在旧时代。")'''
#输入一个英文日期，判断星期几
a=input("请输入英文星期:")
if a=="Tuesday":
    print("星期二")
elif a=="Monday":
    print("星期一")
elif a=="Wednesday":
    print("星期三")
elif a == "Thursday":
    print("星期四")
elif a == "Friday":
    print("星期五")
elif a=="Saturday":
    print("星期六")
elif a == "Sunday":
    print("星期日")
else:
    print("错误")