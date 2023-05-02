import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from pageobjectmodule.amazon import Amzon_search


class Test_jungle:

    url = 'https://www.amazon.in/'
    input_product = "iphone13"

    def test_serach(self,setup):
        self.driver= setup
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.am_se = Amzon_search(self.driver)
        self.am_se.click_serach(self.input_product)
        self.am_se.click_on_serach()
        self.am_se.time()
        self.am_se.product_click()
        self.am_se.time()
        self.am_se.switch_to_window()
        self.am_se.time()
        self.am_se.match_card_details()
        assert self.am_se.nameof_product.text == self.am_se.nameof_product.text
        print('pass')
        time.sleep(4)
        self.am_se.click_addto_card()
        # self.am_se.click_on_proceed()













