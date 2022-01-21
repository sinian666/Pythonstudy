from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://192.168.0.207/ecshop")
time.sleep(3)
#css选择器定位
#搜索
search = driver.find_element_by_css_selector('#keyword')
search.send_keys('手机')
seabtn = driver.find_element_by_css_selector('.go')
seabtn.click()
time.sleep(3)
#注册
regbtn = driver.find_element_by_css_selector('#ECS_MEMBERZONE > a:nth-child(3) > img:nth-child(1)')
regbtn.click()
time.sleep(2)
#id定位
name = driver.find_element_by_id('username')
name.send_keys('lisi003')
#classname定位
inps = driver.find_elements_by_class_name('inputBg')
print(len(inps))
inps[2].send_keys('ewrty')
#name定位
pwdcfm = driver.find_element_by_name('confirm_password')
pwdcfm.send_keys('123456')
#tagname定位
ds = driver.find_elements_by_tag_name('div')
print(len(ds))
time.sleep(2)
#linktext定位
gsm = driver.find_element_by_link_text('GSM手机')
gsm.click()
time.sleep(2)
#partiallinktext定位
dou = driver.find_element_by_partial_link_text('双模')
dou.click()