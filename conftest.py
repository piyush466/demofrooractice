import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='class')
def setup():

    obj = Service(r'C:\\Users\\Cliffex-Lead\\Desktop\\test\\chromedriver.exe')
    driver = webdriver.Chrome(service=obj)
    # driver.get('https://rahulshettyacademy.com/angularpractice/')
    return driver

    # object = Service(r'C:\Users\Cliffex-Lead\Desktop\test\chromedriver.exe')
    # driver = webdriver.Chrome(service=object)
    # driver.get('r"https://rahulshettyacademy.com/angularpractice/')
