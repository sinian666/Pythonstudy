from selenium import webdriver
import time
import csv
from selday02_1.userfuns import regist
driver = webdriver.Firefox()
driver.get("http://192.168.0.207/ecshop")
time.sleep(3)
file = open("E:/python+selenium笔记/regist.csv")
users = csv.reader(file)
for i in users:
    regist(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],driver)

file.close()