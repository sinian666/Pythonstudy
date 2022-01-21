from selenium import webdriver
import time
import unittest
from selday02_1.userfuns import login,regist
class RegistLogin(unittest.TestCase):
    def setUp(self):#打开浏览器
        self.driver = webdriver.Firefox()
        self.driver.get("http://192.168.0.207/ecshop")
        time.sleep(3)
    def tearDown(self): #退出浏览器
        self.driver.quit()
    def testRegist(self):  #注册
        regist("lisi100",'lisi100@163.com','123456','123456','tryhg@163.com','5676543','76543','3245678','87656',6,'aa',self.driver)
    def testlogin(self):  #登录
        login("lisi100" , "123456" , self.driver)
if __name__ == '__main__':
    unittest.main