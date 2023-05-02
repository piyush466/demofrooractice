from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

Object = Service(r"C:\\Users\\Cliffex-Lead\\Desktop\\test\\chromedriver.exe")
driver = webdriver.Chrome(service=Object)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(-2)
driver.find_element(By.LINK_TEXT, "Open Tab").click()
time.sleep(2)
print(driver.current_url)
windows = driver.window_handles
driver.switch_to.window(windows[1])

print(driver.current_url)
print(driver.title)

driver.switch_to.window(windows[0])
print(driver.title)
print(driver.current_url)
driver.execute_script("window.scrollTo(0,1200)")
time.sleep(2)

driver.switch_to.frame("courses-iframe")
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Courses").click()
time.sleep(5)



driver.quit()