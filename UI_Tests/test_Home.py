
import pytest
import allure
import time
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from Links import Links
from locators import Locator
from functions import Functions
from Pages.Home_page import Home


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("choose_stand")
@allure.parent_suite("Home page")
@allure.suite("Home page")
class Test_Home():

    def setup(self):
        self.links = Links()
        self.locators = Locator()
        self.functions = Functions(self.driver)
        self.home = Home(self.driver)

        self.driver.get(self.links.home)


    @pytest.mark.smoke
    @pytest.mark.sanity
    @allure.title("Header menu checking")
    @allure.severity("Critical")
    def test_header_menu(self):

        # Here is wroten open test, because of we have got a problem with HTTPConnection when we try to click on the header's button in turn

        with allure.step("Checking about us button"):
            self.functions.getClick(self.locators.ABOUT_US)
            self.functions.TitleCheck("About Us - SimpleTollFree")
            self.driver.back()

        with allure.step("Checking contact us button"):
            self.functions.getClick(self.locators.CONTACT_US)
            self.functions.TitleCheck("Contact Us - SimpleTollFree")
            self.driver.back()

        with allure.step("Checking faq button"):
            self.functions.getClick(self.locators.FAQ)
            self.functions.TitleCheck("FAQ - SimpleTollFree")
            self.driver.back()

        with allure.step("Checking home button"):
            self.functions.getClick(self.locators.HOME)
            self.functions.TitleCheck("Toll Free Conferencing – Simple Toll Free Conferencing")
            self.driver.back()


    @pytest.mark.smoke
    @pytest.mark.sanity
    @allure.title("Bottom menu checking")
    @allure.severity("Critical")
    def test_bottom_menu(self):

        with allure.step("Checking about us bottom button"):
            self.home.click_on_about_us_bottom_button()

        with allure.step("Checking contact us bottom button"):
            self.home.click_on_contact_us_bottom_button()

        with allure.step("Checking faq bottom button"):
            self.home.click_on_faq_bottom_button()

        with allure.step("Checking home bottom button"):
            self.home.click_on_home_bottom_button()


    @pytest.mark.smoke
    @pytest.mark.sanity
    @allure.title("Sign up button checking")
    @allure.severity("Critical")
    def test_sign_up_button_checking(self):

        with allure.step("Click on sign up button checking"):
            self.home.click_on_sign_up_button()


    @pytest.mark.smoke
    @pytest.mark.sanity
    @allure.title("Login button checking")
    @allure.severity("Critical")
    def test_login_button_checking(self):

        with allure.step("Click on login button"):
            self.home.click_on_login_button()


    @pytest.mark.smoke
    @pytest.mark.sanity
    @allure.title("Logo link checking")
    @allure.severity("Minor")
    def test_logo_link_checking(self):

        with allure.step("Click on sign up button"):
            self.home.click_on_sign_up_button()

        with allure.step("Click on login button checking"):
            self.home.click_on_logo_link()

