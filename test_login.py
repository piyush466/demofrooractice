import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
def get_data():
    return [

        ("vinay@gmail.com","vin@1223")
        ,("piyus@gmail.com","piyus@1223")
    ]
@pytest.mark.parametrize("username,password",get_data())
def test_login(username,password):
  driver = webdriver.Chrome()
  driver.get("https://www.facebook.com/")
  driver.implicitly_wait(10)
  driver.find_element(By.ID,"email").send_keys(username)
  time.sleep(5)
  driver.find_element(By.ID, "pass").send_keys(password)
  time.sleep(5)