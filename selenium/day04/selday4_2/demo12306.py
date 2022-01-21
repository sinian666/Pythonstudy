from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.12306.cn/index/")
time.sleep(3)
#声明js语句，删除readonly属性
#  .removeAttribute('readonly')
s = "document.getElementById('train_date').removeAttribute('readonly')"
driver.execute_script(s)#执行js语句
#声明js语句，输入日期
#   .value='2021-09-20'
a = "document.getElementById('train_date').value='2021-09-20'"
driver.execute_script(a) #执行js语句
time.sleep(2)

# stu = driver.find_element_by_css_selector('#isStudentDan > i:nth-child(2)')
# stu.click()

#声明js语句，修改class属性值
#  .setAttribute('class','active')
js = "document.getElementById('isStudentDan').setAttribute('class','active')"
#执行js语句
driver.execute_script(js)


