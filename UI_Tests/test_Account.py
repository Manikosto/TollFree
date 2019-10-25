import pytest
import requests
import allure
import time
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from Links import Links
from locators import Locator
from functions import Functions
from Pages.ContactUs_page import ContactUs
from Pages.Account_page import Account
from Pages.Yandex_page import YandexLogin
from Pages.Login_page import LoginPage
from Pages.SignUp_Page import SignUpPage
from data import Data


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("choose_stand")
@allure.parent_suite("Account page")
@allure.suite("Account page checking")
class Test_Account():


    def setup(self):
        self.links = Links()
        self.functions = Functions(self.driver)
        self.signup_page = SignUpPage(self.driver)
        self.account_page = Account(self.driver)
        self.yandex_page = YandexLogin(self.driver)
        self.login_page = LoginPage(self.driver)
        self.session = requests.Session()


        self.driver.get(self.links.account)
        self.login_page.login_in_account()


    @pytest.mark.sanity
    @pytest.mark.xfail
    @allure.title("Account info checking")
    @allure.severity("Minor")
    def test_checking_info(self):
            
        with allure.step("Toll number checking"):
            self.account_page.toll_number_assert()

        with allure.step("Toll-free number checking"):
            self.account_page.tollfree_number_assert()

        with allure.step("Access code checking"):
            self.account_page.accsess_code_assert()

        with allure.step("Host PIN checking"):
            self.account_page.host_pin_assert()

        with allure.step("Playback number checking"):
            self.account_page.playback_number_assert()



    @pytest.mark.sanity
    @allure.title("Time zone checking")
    @allure.severity("Minor")
    def test_timezones_info_checking(self):

        with allure.step("Show only USA time zones"):

            self.account_page.change_zones_click()
            self.account_page.text_timezones_checking("Show all time zones")
            self.account_page.account_timezones_click()
            self.functions.getScreenshot("usazones")

        with allure.step("Show all time zones"):
            self.account_page.change_zones_click()
            self.account_page.text_timezones_checking("Show U.S. only")
            self.account_page.account_timezones_click()
            self.functions.getScreenshot("allzones")


    @pytest.mark.sanity
    @allure.title("Resend info checking")
    @allure.severity("Minor")
    def test_timezones_info_checking(self):

        with allure.step("Show only USA time zones"):

            self.account_page.change_zones_click()
            self.account_page.text_timezones_checking("Show all time zones")
            self.account_page.account_timezones_click()
            self.functions.getScreenshot("usazones")

        with allure.step("Show all time zones"):
            self.account_page.change_zones_click()
            self.account_page.text_timezones_checking("Show U.S. only")
            self.account_page.account_timezones_click()
            self.functions.getScreenshot("allzones")


    @pytest.mark.sanity
    @pytest.mark.smoke
    @allure.title("Resend info")
    @allure.severity("Critical")
    def test_resend_info(self):

        with allure.step("Click on resend info button"):
            self.account_page.click_on_resend_info()
           
        with allure.step("Take data for checking"):
            self.account_page.take_data_for_login()

        with allure.step("Checking letter"):
            self.yandex_page.Autorization(Data.TEST_LOGIN, Data.TEST_PASSWORD)
            self.yandex_page.CheckLetter()
            self.functions.getScroll("400")
            self.account_page.checking_information()
