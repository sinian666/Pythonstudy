import time
from selenium.webdriver.support.ui import Select
#登录函数
def login(name, password, driver):
    #点击登录按钮
    logbtn = driver.find_element_by_css_selector('#ECS_MEMBERZONE > a:nth-child(2) > img:nth-child(1)')
    logbtn.click()
    time.sleep(3)
    #输入用户名
    uname = driver.find_element_by_css_selector('.usBox_1 > form:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)')
    uname.send_keys(name)
    #输入密码
    upass = driver.find_element_by_css_selector('.usBox_1 > form:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(1)')
    upass.send_keys(password)
    #点击立即登录按钮
    btn = driver.find_element_by_css_selector('.us_Submit')
    btn.click()
    time.sleep(2)
    #点击退出
    exit = driver.find_element_by_css_selector("#ECS_MEMBERZONE > font:nth-child(2) > a:nth-child(3)")
    exit.click()
    time.sleep(2)

#注册函数
def regist(name,email,pwd,pwdcfm,msn,qq,off,home,phone,question,answer,driver):
    #点击注册按钮
    driver.find_element_by_css_selector('#ECS_MEMBERZONE > a:nth-child(3) > img:nth-child(1)').click()
    time.sleep(3)
    #用户名
    driver.find_element_by_css_selector('#username').send_keys(name)
    #邮箱
    driver.find_element_by_css_selector('#email').send_keys(email)
    #密码
    driver.find_element_by_css_selector('#password1').send_keys(pwd)
    #确认密码
    driver.find_element_by_css_selector('#conform_password').send_keys(pwdcfm)
    #msn
    driver.find_element_by_css_selector('.usBox_2 > form:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2) > input:nth-child(1)').send_keys(msn)
    #qq
    driver.find_element_by_css_selector('.usBox_2 > form:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(2) > input:nth-child(1)').send_keys(qq)
    #办公电话
    driver.find_element_by_css_selector('.usBox_2 > form:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(8) > td:nth-child(2) > input:nth-child(1)').send_keys(off)
    #家庭电话
    driver.find_element_by_css_selector('.usBox_2 > form:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(9) > td:nth-child(2) > input:nth-child(1)').send_keys(home)
    #手机号
    driver.find_element_by_css_selector('.usBox_2 > form:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(10) > td:nth-child(2) > input:nth-child(1)').send_keys(phone)
    #问题
    que = driver.find_element_by_css_selector('.usBox_2 > form:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(2) > select:nth-child(1)')
    qobj = Select(que)
    qobj.select_by_index(question)
    #答案
    driver.find_element_by_css_selector('.usBox_2 > form:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(12) > td:nth-child(2) > input:nth-child(1)').send_keys(answer)
    #立即注册
    driver.find_element_by_css_selector('.us_Submit_reg').click()
    time.sleep(2)
    #退出
    driver.find_element_by_css_selector('#ECS_MEMBERZONE > font:nth-child(2) > a:nth-child(3)').click()
    time.sleep(3)
