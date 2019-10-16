import selenium
import allure
import pytest
import datetime
from data import Data
from locators import Locator
from functions import Functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Pages.BasePage import BasePage

class SignUpPage(BasePage):

    EMAIL = (By.XPATH, Locator.EMAIL)
    SUBMIT = (By.XPATH, Locator.SUBMIT)
    FIRST_NAME = (By.XPATH, Locator.FIRST_NAME)
    LAST_NAME = (By.XPATH, Locator.LAST_NAME)
    PHONE_NUM = (By.XPATH, Locator.PHONE_NUM)
    COMPANY_NAME = (By.XPATH, Locator.COMPANY_NAME)
    CARD_NUMBER = (By.XPATH, Locator.CARD_NUMBER)
    CVV = (By.XPATH, Locator.CVV)
    CARD_HOLDER_NAME = (By.XPATH, Locator.CARD_HOLDER_NAME)
    TERMS_CONDITIONS = (By.XPATH, Locator.TERMS_CONDITIONS)
    STREET_ADDRESS = (By.XPATH, Locator.STREET_ADDRESS)
    SUITE = (By.XPATH, Locator.SUITE)
    CITY = (By.XPATH, Locator.CITY)
    ZIP = (By.XPATH, Locator.ZIP)
    SAME_ABOVE = (By.XPATH, Locator.SAME_ABOVE)
    LOGIN = (By.XPATH, Locator.LOGIN)

    CARD_TYPE = (By.XPATH, Locator.CARD_TYPE)  # SELECT
    MM = (By.XPATH, Locator.MM) # SELECT
    YYYY = (By.XPATH, Locator.YYYY)  # SELECT
    STATE = (By.XPATH, Locator.STATE)


    SIGNUP_TOLL = (By.XPATH, Locator.SIGNUP_TOLL)
    SIGNUP_ACCESS = (By.XPATH, Locator.SIGNUP_ACCESS)
    SIGNUP_PIN = (By.XPATH, Locator.SIGNUP_PIN)

    EMAIL_NUMBER = (By.XPATH, Locator.EMAIL_NUMBER)
    EMAIL_ACCESS_CODE = (By.XPATH, Locator.EMAIL_ACCESS_CODE)
    EMAIL_HOST_PIN = (By.XPATH, Locator.EMAIL_HOST_PIN)




    def enter_customer_info(self):
        self.driver.find_element(*self.FIRST_NAME).send_keys(Data.REG_FIRST_NAME)
        self.driver.find_element(*self.LAST_NAME).send_keys(Data.REG_LAST_NAME)
        self.driver.find_element(*self.EMAIL).send_keys(Data.TEST_LOGIN)
        self.driver.find_element(*self.PHONE_NUM).send_keys(Data.REG_PHONE_NUM)
        self.driver.find_element(*self.COMPANY_NAME).send_keys(Data.REG_COMPANY_NAME)

    def enter_customer_address(self):
        self.driver.find_element(*self.STREET_ADDRESS).send_keys(Data.REG_STREET_ADDRESS)
        self.driver.find_element(*self.SUITE).send_keys(Data.REG_SUITE)
        self.driver.find_element(*self.CITY).send_keys(Data.REG_CITY)
        Select(self.driver.find_element(*self.STATE)).select_by_index(4)
        self.driver.find_element(*self.ZIP).send_keys(Data.REG_ZIP)

    def enter_card_information(self):
        Select(self.driver.find_element(*self.CARD_TYPE)).select_by_index(4)
        self.driver.find_element(*self.CARD_NUMBER).send_keys(Data.CARD)
        Select(self.driver.find_element(*self.MM)).select_by_index(10)
        Select(self.driver.find_element(*self.YYYY)).select_by_index(5)
        self.driver.find_element(*self.CVV).send_keys(Data.CVV_CODE)
        self.driver.find_element(*self.CARD_HOLDER_NAME).send_keys(Data.REG_CARD_HOLDER_NAME)
        self.driver.find_element(*self.TERMS_CONDITIONS).click()

    def submit_click(self):
        self.driver.find_element(*self.SUBMIT).click()

    def take_data_for_login(self):
        self.SignUp_Toll = self.driver.find_element(*self.SIGNUP_TOLL).text
        self.SignUp_Access = self.driver.find_element(*self.SIGNUP_ACCESS).text
        self.SignUp_PIN = self.driver.find_element(*self.SIGNUP_PIN).text

    def checking_information(self):
        self.LOG_number = self.driver.find_element(*self.EMAIL_NUMBER).text
        self.LOG_access_code = self.driver.find_element(*self.EMAIL_ACCESS_CODE).text
        self.LOG_host_pin = self.driver.find_element(*self.EMAIL_HOST_PIN).text

        assert self.SignUp_Toll, self.LOG_number
        assert self.SignUp_Access, self.LOG_access_code
        assert self.SignUp_PIN, self.LOG_host_pin

    def create_file_with_subscriptions(self):
        subscription = open("subscriptions.txt", "a")
        subscription.write(str(datetime.date.today()))
        subscription.write("\n")
        subscription.write("Toll number : " + self.LOG_number + "\n")
        subscription.write("Access code : " + self.LOG_access_code + "\n")
        subscription.write("Host PIN : " + self.LOG_host_pin + "\n")
        subscription.write("\n")
        subscription.close()



    def required_fields(self):
        self.submit_click()
        self.functions.WaitLocate(self.Locator.R_FIELD)