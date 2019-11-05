import pytest
import allure
import time
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.SignUp_Page import SignUpPage
from data import Data
from Links import Links
from locators import Locator
from functions import Functions
from Pages.Yandex_page import YandexLogin


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("choose_stand")
@allure.parent_suite("Sign up page")
@allure.suite("Sign up page")
class Test_SignUp():

    def setup(self):
        self.links = Links()
        self.functions = Functions(self.driver)
        self.signup_page = SignUpPage(self.driver)
        self.yandex_page = YandexLogin(self.driver)

        self.driver.get(self.links.sign_up)

    @pytest.mark.sanity
    @pytest.mark.smoke
    @allure.title("Successful registration")
    @allure.severity("Critical")
    def test_signup(self):

        with allure.step("Title checking"):
            self.functions.TitleCheck("Registration Page - SimpleTollFree")

        with allure.step("Enter Customer Information"):
            self.signup_page.enter_customer_info()
            self.functions.getScreenshot("CustomerInfo")

        with allure.step("Enter Customer Address"):
            self.signup_page.enter_customer_address()
            self.functions.getScreenshot("CustomerAddress")

        with allure.step("Enter Card Information"):
            self.signup_page.enter_card_information()
            self.functions.getScreenshot("CardInfo")

        with allure.step("Click submit"):
            self.signup_page.submit_click()

        with allure.step("Successful registration"):
            self.functions.WaitLocate(Locator.THANK_YOU)
            self.functions.TitleCheck("Account Information - SimpleTollFree")
            self.functions.getScroll("200")
            self.signup_page.take_data_for_login()
            self.functions.getScreenshot("registration")

        with allure.step("Checking letter"):
            self.yandex_page.Autorization(Data.TEST_LOGIN, Data.TEST_PASSWORD)
            self.yandex_page.CheckLetter()
            self.functions.getScroll("400")
            self.signup_page.checking_information()
            self.signup_page.create_file_with_subscriptions()
        with allure.step("Clear email"):
            self.yandex_page.EmptyEmail()

    @pytest.mark.sanity
    @allure.title("Required fields")
    @allure.severity("Minor")
    def test_required_fields(self):

        with allure.step("Title checking"):
            self.functions.TitleCheck("Registration Page - SimpleTollFree")

        with allure.step("Required fields"):
            self.signup_page.required_fields()
            self.functions.getScreenshot("required_fields")




