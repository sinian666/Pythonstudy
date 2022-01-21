#导入模块
from selenium import webdriver
import time
#创建浏览器驱动
a = webdriver.Firefox()
#打开网页
a.get("http://192.168.0.207/ecshop")
time.sleep(3)  #等待
#浏览器最大化
a.maximize_window()
#定位登录按钮
logbtn = a.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[1]/font/a[1]")
#点击登录按钮
logbtn.click()
time.sleep(2)
#定位用户名输入框
name = a.find_element_by_xpath('/html/body/div[7]/div[1]/form/table/tbody/tr[1]/td[2]/input')
name.send_keys("zhaoying001")#输入用户名
#定位密码输入框
password = a.find_element_by_xpath('/html/body/div[7]/div[1]/form/table/tbody/tr[2]/td[2]/input')
password.send_keys('123456')#输入密码
#定位立即登录按钮
button = a.find_element_by_xpath('/html/body/div[7]/div[1]/form/table/tbody/tr[4]/td[2]/input[3]')
#点击立即登录按钮
button.click()
#断言：比较预期结果和实际结果
#定位结果中显示的用户名
result = a.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[1]/font/font/font')
#获取用户名
resname = result.text  #实际结果
#预期结果和实际结果比较
#assert 比较预期结果和实际结果 , "比较失败错误消息"
assert resname == "zhaoying001" , "登录结果用户名与预期不一致"
