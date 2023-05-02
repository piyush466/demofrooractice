import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_experimental_option("debuggerAddress","localhost:9222")
driver = webdriver.Chrome(options=chrome_options)
#
# driver.get('http://cliffex:Cliffex@98765@dev.getcreator.in/')
# driver.maximize_window()
# time.sleep(4)
# driver.find_element(By.XPATH,"//li/a[text()='Login']").click()
#
# driver.find_element(By.XPATH, "//input[@type='email']").send_keys("piyushm@yopmail.com")
# time.sleep(2)
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# time.sleep(2)
# driver.find_element(By.NAME, "password").send_keys("Piyush@123")
# time.sleep(2)
# driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.find_element(By.LINK_TEXT, "Completed Projects").click()

