'''7、应征入伍：
	条件：男，身高170厘米以上，20--26周岁。
	女，身高162厘米以上，20---22周岁之间。
从键盘输入性别，年龄以及身高，判断是否可以应征入伍！
'''
a=input("性别：")
b=int(input("年龄："))
c=float(input("身高："))
if a=="男" and b>=20 and b<=26 and c>170.00:
    print("可以应征入伍")
elif a == "女" and b >= 20 and b <= 22 and c > 162.00:
    print("可以应征入伍")
else:
    print("不可以应征入伍")
