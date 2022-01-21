from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
driver = webdriver.Firefox()
driver.get("http://192.168.0.207/ecshop")
time.sleep(3)
#注册
regbtn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[1]/font/a[2]/img')
regbtn.click()
time.sleep(3)
#用户名
name = driver.find_element_by_xpath('//*[@id="username"]')
name.send_keys('lisi002')
#邮箱
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('lisi002@163.com')
#密码
password = driver.find_element_by_xpath('//*[@id="password1"]')
password.send_keys('123456')
#确认密码
passcfm = driver.find_element_by_xpath('//*[@id="conform_password"]')
passcfm.send_keys('123456')
#msn
msn = driver.find_element_by_xpath('/html/body/div[7]/div/form/table/tbody/tr[6]/td[2]/input')
msn.send_keys('89248@qq.com')
#qq
qq = driver.find_element_by_xpath('/html/body/div[7]/div/form/table/tbody/tr[7]/td[2]/input')
qq.send_keys('56790567')
#办公电话
offphone = driver.find_element_by_xpath('/html/body/div[7]/div/form/table/tbody/tr[8]/td[2]/input')
offphone.send_keys('45678909865')
#家庭电话
homephone = driver.find_element_by_xpath('/html/body/div[7]/div/form/table/tbody/tr[9]/td[2]/input')
homephone.send_keys('67654676')
#手机号
phone = driver.find_element_by_xpath('/html/body/div[7]/div/form/table/tbody/tr[10]/td[2]/input')
phone.send_keys('9097654')
#问题
question = driver.find_element_by_xpath('/html/body/div[7]/div/form/table/tbody/tr[11]/td[2]/select')
queobj = Select(question)
queobj.select_by_index(6)
#答案
answer = driver.find_element_by_xpath('/html/body/div[7]/div/form/table/tbody/tr[12]/td[2]/input')
answer.send_keys('67uiiyty')
#立即注册
btn = driver.find_element_by_xpath('/html/body/div[7]/div/form/table/tbody/tr[14]/td[2]/input[3]')
btn.click()

#实际结果
regname = driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[1]/font/font/font')
nametxt = regname.text  #实际结果
#断言
assert nametxt == "lisi002",'注册bug'

