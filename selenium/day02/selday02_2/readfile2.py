#读文件中的内容，将文件中的大写字母转换为小写字母
#并输出转换后的结果
file = open("E:/python笔记/b.txt")
s = file.read()
for i in s:
    if i.isupper():
        print(i.lower())

file.close()