from selenium import webdriver
import time
from selday02_1.userfuns import regist
driver = webdriver.Firefox()
driver.get("http://192.168.0.207/ecshop")
time.sleep(3)
regist("lisi003",'lisi003@163.com','123456','123456','56543@163.com','76453','65789','876543','57689',6,'aaa',driver)
regist('lisi004','lisi004@163.com','123456','123456','67890@163.com','67897654','6764532','45678654','76543',3,'bb',driver)

