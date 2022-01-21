from selenium import webdriver
import time
#from 包名.文件名 import 函数名
from selday02_1.userfuns import login
driver = webdriver.Firefox()
driver.get("http://192.168.0.207/ecshop")
time.sleep(3)
#调用函数
login("zhaoying001", '123456', driver)
login('zhaoying002', '123456', driver)
login('zhaoying003', '123456', driver)
