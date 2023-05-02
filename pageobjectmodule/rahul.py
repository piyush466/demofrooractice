from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver

class Rahul:

    name_byname = "name"
    email_byname = "email"
    password= "#exampleInputPassword1"
    checkbox1 ="#exampleCheck1"
    radio_button ="//div[@class='form-check form-check-inline']/label"
    birthdate = "bday"
    submitted ="//input[@value='Submit']"

    def __init__(self, driver):
        self.driver = driver

    def name(self,username):
        self.driver.find_element(By.NAME,self.name_byname).send_keys(username)

    def email(self, mail):
        self.driver.find_element(By.NAME, self.email_byname).send_keys(mail)

    def passwords(self,passs):
        self.driver.find_element(By.CSS_SELECTOR, self.password ).send_keys(passs)

    def checkbox(self):
        self.driver.find_element(By.CSS_SELECTOR, self.checkbox1).click()

    def drop_down(self):
        self.select = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        self.select.select_by_visible_text("Female")

    def radio_btn(self):
        self.names = self.driver.find_elements(By.XPATH, self.radio_button)

        for name in self.names:
            print(name.text)
            if name.text == "Employed":
                name.click()

    def selectbirthdate(self,bday):
        self.driver.find_element(By.NAME, self.birthdate).send_keys(bday)

    def submit(self):
        self.driver.find_element(By.XPATH, self.submitted).click()












