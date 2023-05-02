from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_experimental_option("debuggerAddress","localhost:9222")
drivre = webdriver.Chrome(options=chrome_options)
# drivre.get("https://www.facebook.com/")
# drivre.find_element(By.ID,"email").send_keys("piyushdravyakar@gmail.com")

# data=drivre.find_element(By.NAME,'email').send_keys("vinay@gmail.com")
#
drivre.find_element(By.ID,"pass").send_keys("piyush@132")
drivre.find_element(By.NAME, "login").click()

