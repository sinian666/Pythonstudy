from selenium import webdriver
import time
#   import  ActionChains
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get("https://www.163.com/")
time.sleep(5)
#定位悬停的元素
log = driver.find_element_by_css_selector('#js_N_nav_login_title')
#在登录上做悬停操作
ActionChains(driver).move_to_element(log).perform()
time.sleep(3)
#定位浮动框  #js_N_login_wrap > iframe:nth-child(1)
fra = driver.find_element_by_css_selector('#js_N_login_wrap > iframe:nth-child(1)')
#选择浮动框
driver.switch_to.frame(fra)
#定位邮箱输入框
# #account-box > div:nth-child(2) > input:nth-child(2)
email = driver.find_element_by_css_selector('#account-box > div:nth-child(2) > input:nth-child(2)')
email.send_keys('abcd@163.com')