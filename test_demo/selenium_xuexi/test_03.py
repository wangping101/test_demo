from selenium import webdriver
import time
driver = webdriver.PhantomJS()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("yoyo")
driver.find_element_by_id("su").click()
time.sleep(2)
