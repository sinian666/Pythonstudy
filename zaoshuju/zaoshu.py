# -*- coding: utf-8 -*-
import pandas as pd
from faker import Faker
import random
import numpy as np

fake = Faker("zh_CN") # 初始化，可生成中文数据

#设置字段
#index = []
for i in range(1,13):#这里可以设置想要输出的列数，通过增加xi的方式
	exec('x'+str(i)+'=[]')

#设置样本
prod_cd = ['W00028','W00021','W00022']
prod_nm = ['微信支付','银联扫码支付','转账']
channel = ['APP','网银','短信']
year = ['2019','2020','2021']

#循环生成数据20行，具体多少行可以根据需求修改
a=10#此处设置生成的数据个数
for i in range(a):
	# date = random.choice(year)+fake.date()[4:]

	# x1.append('1'+str(fake.random_number(digits=8))) # 随机数字，参数digits设置生成的数字位数
	# x2.append(fake.name())
	# x3.append(fake.ssn()) # 身份证
	# x4.append(random.choice('男女'))
	# x5.append(random.randint(18,25))
	# x6.append(fake.job())
	# x7.append(random.randint(0,1000000))
	# x8.append(random.choice(prod_cd))
	# x9.append(random.choice(prod_nm))
	# x10.append(random.choice(channel))
	# x11.append(date)
	x1.append("".join(random.sample("1234567890qwertyuioplkjhgfdsazxcvbnm", 18)))

#创建数据表
datas = pd.DataFrame({
	# 'user_id':x1,
	# 'name':x2,
	# 'ID_card':x3,
	# 'gender':x4,
	# 'age':x5,
	# 'job':x6,
	# 'salary':x7,
	# 'product_id':x8,
	# 'product':x9,
	# 'channel':x10,
	# 'prt_dt':x11,
	'did':x1
	})

#DataFrame类的to_csv()方法输出数据内容，不保存行索引和列名
datas.to_csv('customer.csv',encoding='utf-8',index=False,header=True)
