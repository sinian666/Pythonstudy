'''4、一水果店售货员算账：已知苹果每斤2.50元，
鸭梨每斤1.80元，香蕉每斤2元，桔子每斤1.6元，
要求输入各类水果的重量，打印出应付钱数，
再输入顾客付款数，打印出应找的钱数。'''
a=float(input("苹果重量："))
b=float(input("鸭梨重量："))
c=float(input("香蕉重量："))
d=float(input("桔子重量："))
y=2.50*a+1.80*b+2.0*c+1.6*d
print("应付钱数=",y,"元")
e=float(input("顾客付款:"))
f=float(e-y)
print("应找的钱数:",f)