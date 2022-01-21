from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://192.168.0.207/ecshop")
time.sleep(3)
#点击登录
driver.find_element_by_css_selector('#ECS_MEMBERZONE > a:nth-child(2) > img:nth-child(1)').click()
time.sleep(2)
#点击立即登录
driver.find_element_by_css_selector('.us_Submit').click()
time.sleep(2)
a = driver.switch_to.alert#选择弹框
s = a.text#获取弹框上的文字
print(s)
a.accept() #点击弹框上的确定按钮
