import pytest
import allure
import time
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from Links import Links
from locators import Locator
from functions import Functions
from Pages.Login_page import LoginPage
from env import env

@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("choose_stand")
@allure.parent_suite(env)
@allure.suite("Login page")
class Test_LoginPage():

    def setup(self):
        self.links = Links()
        self.locators = Locator()
        self.functions = Functions(self.driver)
        self.login_page = LoginPage(self.driver)

        self.driver.get(self.links.login)


    @pytest.mark.smoke
    @pytest.mark.lol
    @pytest.mark.sanity
    @allure.title("Correct login")
    @allure.severity("Critical")
    def test_login(self):

        with allure.step("Login in account"):
            self.login_page.login_in_account()
            self.functions.getScreenshot("Login")

        with allure.step("Account page title checking"):
            self.functions.TitleCheck(Locator.ACCOUNT_INFO)
