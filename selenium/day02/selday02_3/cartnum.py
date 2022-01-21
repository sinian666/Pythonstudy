from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://192.168.0.207/ecshop")
time.sleep(3)
#点击商品
driver.find_element_by_css_selector('#show_best_area > div:nth-child(1) > a:nth-child(2) > img:nth-child(1)').click()
time.sleep(2)
#修改数量
nums = driver.find_element_by_css_selector('#number')
nums.clear()
nums.send_keys(3)
#选中黑色
driver.find_element_by_css_selector('#spec_value_226').click()
time.sleep(2)
#加入购物车
driver.find_element_by_css_selector('li.padd:nth-child(9) > a:nth-child(1) > img:nth-child(1)').click()
time.sleep(3)
#修改购买数量
cnums = driver.find_element_by_css_selector('#formCart > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(5) > input:nth-child(1)')
cnums.clear()
cnums.send_keys(1)


