import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome = Service()
driver= webdriver.Chrome(service=chrome)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME,"name").send_keys("piyush")
driver.find_element(By.NAME, "email").send_keys("piyush@gmail.com")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").send_keys("Piyush@123")
driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()
time.sleep(2)
select = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
select.select_by_visible_text("Female")
time.sleep(2)
names = driver.find_elements(By.XPATH, "//div[@class='form-check form-check-inline']/label")

for name in names:
    print(name.text)
    if name.text == "Employed":
        name.click()
time.sleep(2)

driver.find_element(By.NAME, "bday").send_keys("28-04-1999")
driver.find_element(By.XPATH, "//input[@value='Submit']").click()
time.sleep(2)

succes = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']")
print(succes.text)
time.sleep(2)

assert succes.text == 'Success! The Form has been submitted successfully!.', 'Test fail'


