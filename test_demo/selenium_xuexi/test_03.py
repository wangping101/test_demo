from selenium import webdriver
import time
import cx_Oracle
import urllib3
from bs4 import BeautifulSoup
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("yoyo")
driver.find_element_by_id("su").click()
time.sleep(2)
