import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Amzon_search:

    search_ID = "twotabsearchtextbox"

    click_serach_btn_xpath = "//input[@type='submit']"
    click_product_xpath = "(//div[@class='a-section aok-relative s-image-fixed-height'])[1]"
    add_product = "#add-to-cart-button"
    card_name_Css = "#productTitle"
    click_card_css = "#nav-cart-count"
    name_mtch = "(//span[text()='Apple iPhone 14 (128 GB) - Yellow'])[1]"

    add_card_btn_css = "#add-to-cart-button"
    click_on_cart = '(//form/span/span/input)[6]'
    # "//form/span/span/input
    proceed = "proceedToRetailCheckout"

    def __init__(self,driver):
        self.driver = driver

    def click_serach(self,input_product):
        self.driver.find_element(By.ID,self.search_ID).send_keys(input_product)

    def click_on_serach(self):
        self.driver.find_element(By.XPATH, self.click_serach_btn_xpath).click()

    def product_click(self):
        self.driver.find_element(By.XPATH, self.click_product_xpath).click()

    def switch_to_window(self):
        self.chwnd = self.driver.window_handles[1]
        self.driver.switch_to.window(self.chwnd)
        # print(self.driver.title)
        print("pass")
        self.driver.find_element(By.CSS_SELECTOR, self.add_product).click()

    def time(self):
        time.sleep(2)

    def match_card_details(self):
        self.nameof_product = self.driver.find_element(By.CSS_SELECTOR,self.card_name_Css)
        print(self.nameof_product.text)

    def click_addto_card(self):
        # self.driver.refresh()
        time.sleep(4)
        self.driver.find_element(By.CSS_SELECTOR, self.add_card_btn_css).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//form/span/span/input").click()



        #
        # self.action = ActionChains(self.driver)
        # self.action.move_to_element("//*[@id=\'attach-accessory-pane\']/div/div[1]").build().perform()























