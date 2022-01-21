from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://192.168.0.207/ecshop")
time.sleep(3)
#搜索输入框
search = driver.find_element_by_css_selector('#keyword')
search.send_keys('手机')
time.sleep(2)
#清空文本框
search.clear()
search.send_keys('耳机')
time.sleep(2)
#获取文本框中的内容
content = search.get_property('value')
print(content)
