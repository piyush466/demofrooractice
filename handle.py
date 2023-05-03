import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# driver.find_element(By.CSS_SELECTOR, "#opentab").click()
# #handle windows
# window = driver.window_handles
# driver.switch_to.window(window[1])
# print(driver.current_url)
# time.sleep(2)
# driver.switch_to.window(window[0])
# driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()
# time.sleep(2)
# # alert = Alert(driver)
# # print(alert.text)
# alert = driver.switch_to.alert
# alert.dismiss()
# print(alert.text)
# time.sleep(2)
# print("accept")
# time.sleep(2)
# select = Select(driver.find_element(By.ID, "dropdown-class-example"))
# select.select_by_value("option2")
# time.sleep(2)
#
# select.select_by_visible_text("Option3")
# time.sleep(2)
# select.select_by_index(1)
time.sleep(2)
#
# driver.find_element(By.CSS_SELECTOR, "#openwindow").click()
# id=driver.window_handles
# print(id)
# time.sleep(5)
# id2= driver.current_window_handle
# print(id2)
# time.sleep(5)
# # new = driver.switch_to.new_window()
# # driver.switch_to.new_window(new[1])
# # time.sleep(7)
# # print(driver.current_url)
#
# t=driver.switch_to.window(id[1])
# print(t)
# print(" hogya hai ")
# # tet=driver.find_element(By.XPATH,'//*[@id="header-part"]/div[2]/div/div/div[2]/div/div[1]/div[2]/span').text
# # print(tet)

# driver.find_element(By.CSS_SELECTOR, "#openwindow").click()
#
# print(driver.current_url)
# test = driver.window_handles
# print(test)
# new_wind = driver.switch_to.window(test[1])
# print(driver.current_url)
# test = driver.find_element(By.XPATH,"/html/body/header/div[1]/div/div/div[1]/div/ul/li[1]/span")
# print(test.text)
# test0 = driver.window_handles
# driver.switch_to.window(test0[0])
# print(driver.current_url)
# print(driver.title)

#
# test = driver.window_handles
# print(test)
# time
# driver.find_element(By.CSS_SELECTOR, "#openwindow").click()
# time.sleep(5)
# id= driver.current_window_handle
# print(id)
# # if id in test:
# #     driver.switch_to.window(id)
# #     test = driver.find_element(By.XPATH,"/html/body/header/div[1]/div/div/div[1]/div/ul/li[1]/span")
# #     print(test.text)
#
# time.sleep(5)

# driver.find_element(By.ID,'name').send_keys(" piyush tester ")
# driver.find_element(By.ID,'alertbtn').click()
#
#
# test=driver.switch_to.alert
#
# print(test.text)
#
# time.sleep(5)


# locte= driver.find_element(By.ID,'mousehover')
# print(locte.location)
#
# driver.execute_script("window.scrollBy(23,1374)")
#
#
# act= ActionChains(driver)
# act.move_to_element(locte).perform()
#
# time.sleep(2)
#
# driver.find_element(By.LINK_TEXT,'Top').click()
# time.sleep(5)



driver.find_element(By.ID,'autocomplete').send_keys('in')
time.sleep(5)

a=True

# while a:
 # for name in country_name:
country_name = driver.find_elements(By.XPATH, '//*[@id="ui-id-1"]/li')
for name in country_name:

    print(name.text)
    if name.text.endswith('dia'):
        print(name.text)
        name.click()
        break
    # a=False

time.sleep(10)



