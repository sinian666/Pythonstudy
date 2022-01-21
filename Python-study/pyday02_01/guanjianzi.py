for i in range(1,10):#到5以后就不执行了。
    print(i)
    if i==5:
        break
for i in range(1, 10):  # 在5的时候就不往下执行了。
    if i == 5:
        break
    print(i)
for i in range(1, 10):  # 在5的时候就不执行continue后面的内容了。
    if i == 5:
        continue
    print(i)