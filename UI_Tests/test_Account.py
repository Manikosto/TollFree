import pytest
import allure
import time
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from Links import Links
from locators import Locator
from functions import Functions
from Pages.ContactUs_page import ContactUs
from Pages.Account_page import Account
from Pages.Login_page import LoginPage


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("choose_stand")
@allure.parent_suite("Account page")
class Test_Account():


    def setup(self):
        self.links = Links()
        self.functions = Functions(self.driver)
        self.contact_page = ContactUs(self.driver)
        self.account_page = Account(self.driver)
        self.login_page = LoginPage(self.driver)

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

        with allure.step("First name checking"):
            self.account_page.first_name_assert()

        with allure.step("Last name checking"):
            self.account_page.last_name_assert()

        with allure.step("Email checking"):
            self.account_page.email_assert()

        with allure.step("Phone number checking"):
            self.account_page.phone_number_assert()

        with allure.step("Company name checking"):
            self.account_page.company_name_assert()

        with allure.step("Street address checking"):
            self.account_page.address_assert()

        with allure.step("Suite checking"):
            self.account_page.suite_assert()

        with allure.step("Zip checking"):
            self.account_page.zip_assert()

        with allure.step("State checking"):
            self.account_page.state_assert()



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
