'''8、输入三门课的成绩，按格式显示每门课的成绩。
计算Java和SQL的成绩差，再计算3门课的平均分'''
a=int(input("STB的成绩是："))
b=int(input("Java的成绩是："))
c=int(input("SQL的成绩是："))
print('-----------------------')
print("STB"'  '"Java"'  '"SQL")
print(a,'  ',b,'  ',c)
print('-----------------------')
d=b-c
print('Java和SQL的成绩差:',d)
e=(a+b+c)/3
print('3门课的平均分:',e)