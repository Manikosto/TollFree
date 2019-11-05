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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class LoginPage(BasePage):

    LOGO =(By.XPATH, Locator.LOGO)
    SIGN_UP =(By.XPATH, Locator.SIGN_UP)
    LOGIN =(By.XPATH, Locator.LOGIN)
    HOME =(By.XPATH, Locator.HOME)
    CONTACT_US =(By.XPATH, Locator.CONTACT_US)
    FAQ =(By.XPATH, Locator.FAQ)
    ABOUT_US =(By.XPATH, Locator.ABOUT_US)
    HOME_BUTTON =(By.XPATH, Locator.HOME_BUTTON)
    CONTACT_BOTTOM =(By.XPATH, Locator.CONTACT_BOTTOM)
    FAQ_BOTTOM =(By.XPATH, Locator.FAQ_BOTTOM)
    ABOUT_BOTTOM =(By.XPATH, Locator.ABOUT_BOTTOM)


    DIAL_NUMBER =(By.XPATH, Locator.DIAL_NUMBER)
    ACCESSCODE =(By.XPATH, Locator.ACCESSCODE)
    HOST_PIN =(By.XPATH, Locator.HOST_PIN)
    REMEMBER_ME =(By.XPATH, Locator.REMEMBER_ME)
    SUBMIT =(By.XPATH, Locator.SUBMIT)
    FORGOT_PASS =(By.XPATH, Locator.FORGOT_PASS)
    SEND_INFO =(By.XPATH, Locator.SEND_INFO)



    def get_dial_number(self):
        return self.driver.find_element(*self.DIAL_NUMBER)

    def get_accesscode(self):
        return self.driver.find_element(*self.ACCESSCODE)

    def get_host_pin(self):
        return self.driver.find_element(*self.HOST_PIN)

    def remember_me_button_click(self):
        return self.driver.find_element(*self.REMEMBER_ME).click()

    def submit_button_click(self):
        return self.driver.find_element(*self.SUBMIT).click()


    def login_in_account(self):
        self.functions.TitleCheck("Login - SimpleTollFree")
        self.get_dial_number().send_keys(Data.CORRECT_DIAL)
        self.get_accesscode().send_keys(Data.CORRECT_ACCESS)
        self.get_host_pin().send_keys(Data.CORRECT_PIN)
        self.remember_me_button_click()
        self.submit_button_click()
        self.functions.WaitLocate(Locator.PAGE_NAME)
