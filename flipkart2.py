import time

from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button").click()

driver.find_element(By.XPATH, "//input[@name='q']").send_keys("iphone11")
time.sleep(2)

driver.find_element(By.XPATH, "//button[@class='L0Z3Pu']").click()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "iPhone 11").click()
time.sleep(2)

window = driver.window_handles
driver.switch_to.window(window[1])
time.sleep(3)
driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2U9uOA ihZ75k _3AWRsL']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("8411878794")
time.sleep(3)
driver.find_element(By.XPATH, "//span[text()='CONTINUE']").click()
time.sleep(2)










