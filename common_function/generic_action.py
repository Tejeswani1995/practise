
from datetime import datetime
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from inclusive_function.configure import Config
from inclusive_function.wait_decorater import wait


class GenericActions():

    def __init__(self, driver):
        self.driver = driver

    @wait
    def enter_text(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @wait
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def search_element(self, locator):
        webelement_list = self.driver.find_elements(*locator)
        if len(webelement_list) == 1:
            return True
        else:
            return False

    def check_title(self, expected_title):
        wait = WebDriverWait(self.driver, 30)
        if wait.until(EC.title_is(expected_title)):
            return True
        return False



