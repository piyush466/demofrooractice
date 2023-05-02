import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

optionss = Service()
driver = webdriver.Chrome(service=optionss)
driver.get("https://www.amazon.in/OnePlus-Nord-Pastel-128GB-Storage/dp/B0BY8JZ22K/ref=sw_ttl_ts_crc_0?_encoding=UTF8&pd_rd_i=B0BY8JZ22K&pd_rd_w=CA6sP&content-id=amzn1.sym.44c76463-8001-4037-9337-163868cb4589&pf_rd_p=44c76463-8001-4037-9337-163868cb4589&pf_rd_r=HH19R5GRGP25GMC14E93&pd_rd_wg=3boTm&pd_rd_r=5fad2779-e91c-47ec-91e9-c3db697a17b5&th=1")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-button").click()
time.sleep(5)
driver.find_element(By.XPATH, "//form/span/span/input").click()
time.sleep(30)

driver.implicitly_wait(10)