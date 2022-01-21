#导入模块
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
driver = webdriver.Firefox()
driver.get("http://192.168.0.207/ecshop")
time.sleep(3)
#定位下拉列表
cate = driver.find_element_by_xpath('//*[@id="category"]')
#将下拉列表转换为Select类的对象
b = Select(cate)
b.select_by_index(5)#按选项下标选择
time.sleep(3)
b.select_by_value("13")#按选项的value属性值选择
time.sleep(3)
b.select_by_visible_text('手机类型')#按选项的文字选择