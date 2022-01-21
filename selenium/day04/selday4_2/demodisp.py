from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("file:///E:\disp.html")
time.sleep(2)
#  .style.display='block'
s = "document.getElementById('two').style.display='block'"
driver.execute_script(s)