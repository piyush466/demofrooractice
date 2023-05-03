import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#
# opt=Options()
# opt.add_argument("")

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.find_element(By.NAME, "q").send_keys("iphone13")
time.sleep(2)

driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']").click()

driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)
driver.find_element(By.XPATH, "(//div[@class='_4rR01T'])[1]").click()
time.sleep(2)
test = driver.window_handles
driver.switch_to.window(test[1])
driver.find_element(By.XPATH, "//button[@type='button']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("piyush@yopmail.com")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)