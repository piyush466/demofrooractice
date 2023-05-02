import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# chrome = Service(r"C:\\Users\\Cliffex-Lead\\Desktop\\test\\chromedriver.exe")
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.execute_script("window.scrollTo(0,1000)")

time.sleep(2)
action = ActionChains(driver)
time.sleep(2)
action.move_to_element(driver.find_element(By.ID, "mousehover")).click().perform()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Top").click()
time.sleep(2)

driver.execute_script("window.scrollTo(0,1000)")


driver.switch_to.frame("courses-iframe")
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Courses").click()
time.sleep(2)


# piyush dravyakar
print("test good ")

print("hii piyush dravyakar")


print("gwgdywe")




driver.quit()



