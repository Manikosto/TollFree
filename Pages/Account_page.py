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

    def first_name_assert(self):
        assert self.driver.find_element(*self.ACC_FIRST_NAME).get_attribute("value") == self.data.PROF_FIRST_NAME

    def last_name_assert(self):
        assert self.driver.find_element(*self.ACC_LAST_NAME).get_attribute("value") == self.data.PROF_LAST_NAME

    def email_assert(self):
        assert self.driver.find_element(*self.ACC_EMAIL).get_attribute("value") == self.data.PROF_EMAIL

    def phone_number_assert(self):
        assert self.driver.find_element(*self.ACC_PHONE_NUM).get_attribute("value") == self.data.PROF_PHONE_NUMBER

    def company_name_assert(self):
        assert self.driver.find_element(*self.ACC_COMPANY_NAME).get_attribute("value") == self.data.PROF_COMPANY_NAME

    def address_assert(self):
        assert self.driver.find_element(*self.ACC_STREET_ADDRESS).get_attribute("value") == self.data.PROF_ADDRESS

    def suite_assert(self):
        assert self.driver.find_element(*self.ACC_SUITE).get_attribute("value") == self.data.PROF_SUITE

    def zip_assert(self):
        assert self.driver.find_element(*self.ACC_ZIP).get_attribute("value") == self.data.PROF_ZIP

    def state_assert(self):
        assert self.driver.find_element(*self.ACC_STATE).get_attribute("value") == self.data.PROF_STATE



    def change_zones_click(self):
        return self.driver.find_element(*self.ACC_CHANGE_ZONES).click()

    def account_timezones_click(self):
        return self.driver.find_element(*self.ACC_TIMEZONES).click()

    def text_timezones_checking(self, text):
        assert self.driver.find_element(*self.ACC_CHANGE_ZONES).text == text


