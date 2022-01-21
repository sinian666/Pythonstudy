#导入模块
import csv
#打开文件
file = open("E:/python+selenium笔记/login.csv")
#读文件
s = csv.reader(file)
for i in s:
    print("姓名：" , i[0])
    print("性别：" , i[1])
    print("年龄：" , i[2])
file.close()