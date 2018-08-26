from  appium import  webdriver
import  time
import  json
desired_caps = {'platformName': 'Android',
                'platformVersion': '7.0',
                'deviceName': '127.0.0.1:62001',  # T8DDU15A28010857 127.0.0.1:62001
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                # 'automationName': 'Uiautomator2',
                'automationName': 'Appium',
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                'noReset': True,
                'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'} }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(30)
driver.find_element_by_accessibility_id("搜索").click()
driver.implicitly_wait(30)
driver.find_element_by_id('com.tencent.mm:id/hz').send_keys(u"从零开始学自动化")
driver.implicitly_wait(30)
driver.find_element_by_id('com.tencent.mm:id/lp').click()
driver.implicitly_wait(30)
driver.find_element_by_id('com.tencent.mm:id/acn').click()
driver.implicitly_wait(30)
print(driver.contexts)
# driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
driver.implicitly_wait(30)
# driver.find_element_by_xpath(".//*[@id='namespace_1']/div[1]/div/div[2]").click()
driver.find_element_by_accessibility_id('app').click()

driver.implicitly_wait(30)
elementss=driver.find_elements_by_css_selector(".title.js_title")
print(elementss)
for i in elementss:
    print(i.text)
# print(driver.window_handles)
# driver.switch_to_window('CDwindow-5cb503aa-52f7-4edd-aac1-1576fff50b56')
# driver.find_element_by_accessibility_id('app').click()

driver.implicitly_wait(30)
driver.quit()