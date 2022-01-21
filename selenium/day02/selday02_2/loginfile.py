from selenium import webdriver
import time
from selday02_1.userfuns import login
import csv
driver = webdriver.Firefox()
driver.get("http://192.168.0.207/ecshop")
time.sleep(3)
file = open("E:/python+selenium笔记/login.csv")
users = csv.reader(file)
for u in users:
    login(u[0] , u[1] , driver)
file.close()