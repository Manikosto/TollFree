import selenium
import allure
import pytest
import time
from data import Data
from locators import Locator
from functions import Functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Pages.BasePage import BasePage
from selenium.webdriver.common.keys import Keys

class Home(BasePage):
    LOGO = (By.XPATH, Locator.LOGO)
    SIGN_UP = (By.XPATH, Locator.SIGN_UP)
    LOGIN = (By.XPATH, Locator.LOGIN)
    HOME = (By.XPATH, Locator.HOME)
    CONTACT_US = (By.XPATH, Locator.CONTACT_US)
    FAQ = (By.XPATH, Locator.FAQ)
    ABOUT_US = (By.XPATH, Locator.ABOUT_US)
    HOME_BOTTOM = (By.XPATH, Locator.HOME_BUTTON)
    CONTACT_BOTTOM = (By.XPATH, Locator.CONTACT_BOTTOM)
    FAQ_BOTTOM = (By.XPATH, Locator.FAQ_BOTTOM)
    ABOUT_BOTTOM = (By.XPATH, Locator.ABOUT_BOTTOM)


    def click_on_about_us_bottom_button(self):
        self.driver.find_element(*self.ABOUT_BOTTOM).click()
        self.functions.TitleCheck("About Us - SimpleTollFree")
        self.driver.back()

    def click_on_contact_us_bottom_button(self):
        self.driver.find_element(*self.CONTACT_BOTTOM).click()
        self.functions.TitleCheck("Contact Us - SimpleTollFree")
        self.driver.back()

    def click_on_faq_bottom_button(self):
        self.driver.find_element(*self.FAQ_BOTTOM).click()
        self.functions.TitleCheck("FAQ - SimpleTollFree")
        self.driver.back()

    def click_on_home_bottom_button(self):
        self.driver.find_element(*self.HOME_BOTTOM).click()
        self.functions.TitleCheck("Toll Free Conferencing – Simple Toll Free Conferencing")
        self.driver.back()

    def click_on_sign_up_button(self):
        self.driver.find_element(*self.SIGN_UP).click()
        self.functions.TitleCheck("Registration Page - SimpleTollFree")
        self.functions.getScreenshot("SignUp")

    def click_on_login_button(self):
        self.driver.find_element(*self.LOGIN).click()
        self.functions.TitleCheck("Login - SimpleTollFree")
        self.functions.getScreenshot("Login")

    def click_on_logo_link(self):
        self.driver.find_element(*self.LOGO).click()
        self.functions.TitleCheck("Toll Free Conferencing – Simple Toll Free Conferencing")
        self.functions.getScreenshot("Logolink")

