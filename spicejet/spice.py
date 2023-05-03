import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("----disable-notifications")
chrome_options.add_argument("--disable-geolocation")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.spicejet.com/")
driver.implicitly_wait(20)

#
# driver.find_element(By.XPATH, "(//input[@dir='auto'])[2]").send_keys("Mumbai")
# time.sleep(3)

# driver.find_element(By.XPATH, "//div[text()='Fri, 13 May 2023']").click()
# time.sleep(4)

# driver.find_element(By.XPATH, "//*[@id='main-container']/div/div[1]/div[3]/div[2]/div[4]/div/div[1]/div[1]/div[2]/div[2]").click()
# time.sleep(5)
# date =  driver.find_elements(By.XPATH, "/html/body/div[2]/div/div/div[1]/div[3]/div[2]/div[4]/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/div[3]/div/div")
#
# for dat in date:
#     print(dat.text)
#     if dat.text == "28":
#         dat.click()
#         break
#
# time.sleep(4)

driver.find_element(By.XPATH, "//div[text()='1 Adult']").click()
time.sleep(2)

# for n in range(1,4):
#
#     category = driver.find_element(By.XPATH,
#                                     '//*[@id="main-container"]/div/div[1]/div[3]/div[2]/div[5]/div[1]/div/div[2]/div[2]/div/div[1]/div['+str(n)+']/div[1]/div[1]')
#     print(category.text)

#     if category.text=="Adult":
#         for n in range(2):
#             driver.find_element(By.XPATH,'//*[@id="main-container"]/div/div[1]/div[3]/div[2]/div[5]/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[3]').click()
#             print(n)
#             time.sleep(5)
#     if category.text=="Children":
#         for n in range(3):
#             driver.find_element(By.XPATH,
#                                 '//*[@id="main-container"]/div/div[1]/div[3]/div[2]/div[5]/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[3]').click()
#             print(n)
#
#             time.sleep(5)
#
# time.sleep(10)
# driver.find_element(By.XPATH, "//*[@id='main-container']/div/div[1]/div[3]/div[2]/div[5]/div[2]/div").click()
# time.sleep(2)
# currency = driver.find_elements(By.XPATH, "//div[@class='css-1dbjc4n r-1habvwh r-1loqt21 r-1777fci r-1mi0q7o r-1yt7n81 r-m611by r-1otgn73']")
#
# for cor in currency:
#     print(cor.text)
#     if cor.text=="BDT":
#         cor.click()
#         break
#
# time.sleep(3)
#
# radio_btn = driver.find_elements(By.XPATH, "//div[@class='css-1dbjc4n r-1d09ksm r-1inuy60 r-m611by']/div[2]/div/div")
# for radio in radio_btn:
#     print(radio.text)
#     if radio.text == "Students":
#         radio.click()
#
# time.sleep(2)
#
# driver.find_element(By.XPATH, "//*[@id='main-container']/div/div[1]/div[3]/div[2]/div[7]/div[2]/div").click()
#
# time.sleep(3)
#
#
#
#
#
#
#
#
#
#
#
#
#



# driver.find_element(By.XPATH,'//*[@id="main-container"]/div/div[1]/div[3]/div[2]/div[4]/div/div[1]/div[1]/div[2]/div[2]').click()
# time.sleep(5)
#
# date=driver.find_elements(By.XPATH,'//*[@id="main-container"]/div/div[1]/div[3]/div[2]/div[4]/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/div[3]/div/div')
# for n in date:
#     print(n.text)
#     if n.text=='26':
#         n.click()
#         break
#
# time.sleep(5)




drop = driver.find_elements(By.XPATH, "//div[@class='css-76zvg2 r-homxoj r-1i10wst r-1kfrs79']")
plus = driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-1awozwy r-19m6qjp r-y47klf r-1loqt21 r-eu3ka r-1777fci r-1otgn73 r-eafdt9 r-1i6wzkk r-lrvibr r-1aockid'])[2]")
for dr in drop:
    print(dr.text)

    # if dr.text =="Children":

    if dr.text == "Children":
        print("pass")
        print(dr.text)
        for test in range(3):
            plus.click()



            # driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-1awozwy r-19m6qjp r-y47klf r-1loqt21 r-eu3ka r-1777fci r-1otgn73 r-eafdt9 r-1i6wzkk r-lrvibr r-1aockid'])[2]").click()




            # if dr.text=="Children":
            #     pl.click()



time.sleep(5)




