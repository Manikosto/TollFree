import selenium
import allure
import pytest
import time
from data import Data
from locators import Locator
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Links import Links

class Account(BasePage):

    ACC_EMAIL = (By.XPATH, Locator.ACC_EMAIL)
    SUBMIT = (By.XPATH, Locator.SUBMIT)
    ACC_FIRST_NAME = (By.XPATH, Locator.FIRST_NAME)
    ACC_LAST_NAME = (By.XPATH, Locator.ACC_LAST_NAME)
    ACC_PHONE_NUM = (By.XPATH, Locator.ACC_PHONE_NUM)
    ACC_COMPANY_NAME = (By.XPATH, Locator.ACC_COMPANY_NAME)

    ACC_STREET_ADDRESS = (By.XPATH, Locator.ACC_STREET_ADDRESS)
    ACC_SUITE = (By.XPATH, Locator.ACC_SUITE)
    ACC_CITY = (By.XPATH, Locator.ACC_CITY)
    ACC_ZIP = (By.XPATH, Locator.ACC_ZIP)
    ACC_STATE = (By.XPATH, Locator.ACC_STATE)  # SELECT

    TOLL = (By.XPATH, Locator.TOLL)
    TOLLFREE = (By.XPATH, Locator.TOLLFREE)
    ACC_ACCESSCODE = (By.XPATH, Locator.ACC_ACCESSCODE)
    ACC_HOSTPIN = (By.XPATH, Locator.ACC_HOSTPIN)
    ACC_PLAYBACK_NUMBER = (By.XPATH, Locator.ACC_PLAYBACK_NUMBER)
    PROF_STATE_LOCATOR = (By.XPATH, Locator.PROF_STATE_LOCATOR)

    DRP_TIMEZONES = (By.XPATH, Locator.DRP_TIMEZONES) # SELECT
    ACC_TIMEZONES = (By.XPATH, Locator.ACC_TIMEZONES)  # For click
    ACC_CHANGE_ZONES = (By.XPATH, Locator.ACC_CHANGE_ZONES)
    ACC_RESEND_INFO = (By.XPATH, Locator.ACC_RESEND_INFO)

    EMAIL_NUMBER = (By.XPATH, Locator.EMAIL_NUMBER)
    EMAIL_ACCESS_CODE = (By.XPATH, Locator.EMAIL_ACCESS_CODE)
    EMAIL_HOST_PIN = (By.XPATH, Locator.EMAIL_HOST_PIN)


    def toll_number_assert(self):

        assert self.driver.find_element(*self.TOLL).text == self.data.TOLL_NUMBER

    def tollfree_number_assert(self):
        assert self.driver.find_element(*self.TOLLFREE).text == self.data.CORRECT_DIAL

    def accsess_code_assert(self):
        assert self.driver.find_element(*self.ACC_ACCESSCODE).text == self.data.CORRECT_ACCESS

    def host_pin_assert(self):
        assert self.driver.find_element(*self.ACC_HOSTPIN).text == self.data.CORRECT_PIN

    def playback_number_assert(self):
        assert self.driver.find_element(*self.ACC_PLAYBACK_NUMBER).text == self.data.PLAYBACK_NUMBER

    def change_zones_click(self):
        return self.driver.find_element(*self.ACC_CHANGE_ZONES).click()

    def account_timezones_click(self):
        return self.driver.find_element(*self.ACC_TIMEZONES).click()

    def text_timezones_checking(self, text):
        assert self.driver.find_element(*self.ACC_CHANGE_ZONES).text == text

    def click_on_resend_info(self):

        self.driver.find_element(*self.ACC_RESEND_INFO).click()
        self.functions.WaitLocate(self.Locator.RESEND_INFO_MESSAGE)
        self.functions.getScreenshot("resendinfo")

    def take_data_for_login(self):
        self.SignUp_Toll = self.driver.find_element(*self.TOLL).text
        self.SignUp_Access = self.driver.find_element(*self.ACC_ACCESSCODE).text
        self.SignUp_PIN = self.driver.find_element(*self.ACC_HOSTPIN).text

    def checking_information(self):
        self.LOG_number = self.driver.find_element(*self.EMAIL_NUMBER).text
        self.LOG_access_code = self.driver.find_element(*self.EMAIL_ACCESS_CODE).text
        self.LOG_host_pin = self.driver.find_element(*self.EMAIL_HOST_PIN).text

        assert self.SignUp_Toll, self.LOG_number
        assert self.SignUp_Access, self.LOG_access_code
        assert self.SignUp_PIN, self.LOG_host_pin