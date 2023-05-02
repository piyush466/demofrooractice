import time
import logging
import pytest

from baseclass import BaseClass
from pageobjectmodule.rahul import Rahul



@pytest.mark.usefixtures("setup")
class Test_atumation(BaseClass):
    url = 'https://rahulshettyacademy.com/angularpractice/'



    def test_rahul001(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.url)
        log = self.getLogger()
        log.info("This is a information bugs")
        self.rahu = Rahul(self.driver)
        self.rahu.name("piyush")
        log.error("This is a erroer")
        self.rahu.email("piyush@gmail.com")
        time.sleep(2)

        self.rahu.passwords("piyush@123")
        time.sleep(2)

        self.rahu.checkbox()
        self.rahu.drop_down()
        time.sleep(2)
        self.rahu.radio_btn()
        self.rahu.selectbirthdate("04-28-1999")
        self.rahu.submit()

