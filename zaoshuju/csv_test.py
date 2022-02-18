# -*- coding :UTF-8 -*-
# @Time      :2022/2/4 2:25 PM
# @Author    :Si Nian
# @Software  :PyCharm
import pandas as pd
import random

#设置字段
#index = []
for i in range(1,13):#这里可以设置想要输出的列数，通过增加xi的方式
        exec('x'+str(i)+'=[]')
a=3000#此处设置生成的数据个数
for i in range(a):
        x1.append("".join(random.sample("qwertyuioplkjhgfdsazxcvbnm", 18)))
#创建数据表
datas = pd.DataFrame({
        'x-device-id':x1
})
#DataFrame类的to_csv()方法输出数据内容，不保存行索引和列名
datas.to_csv('caculator3k.csv',encoding='utf-8',index=False,header=True)
