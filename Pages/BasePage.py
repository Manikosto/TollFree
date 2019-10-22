import selenium
import allure
import pytest

from data import Data
from locators import Locator
from functions import Functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Links import Links

class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 30)
        self.functions = Functions(self.driver)

        self.links = Links()
        self.Locator = Locator()
        self.data = Data()

    def open_link(self, link):
        return self.driver.get(link)

    def wait_clicable(self, elem):
        self.wait.until(EC.element_to_be_clickable((elem)))