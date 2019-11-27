import pytest
import allure
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from locators import Locator
from Pages.ContactUs_page import ContactUs
from Links import Links
from functions import Functions
from env import env


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("choose_stand")
@allure.parent_suite("Contact Us")
@allure.suite("Contact Us page checking")
class Test_ContactUs():

    def setup(self):
        self.links = Links()
        self.functions = Functions(self.driver)
        self.contact_page = ContactUs(self.driver)

        self.driver.get(self.links.contact_us)


    @pytest.mark.smoke
    @pytest.mark.sanity
    @allure.title("Send form")
    @allure.severity("Critical")
    def test_send_form(self):
        with allure.step("Send contact us form"):
            self.contact_page.send_form("Test", "lol@gmail.com", "89999999999", "Hello")
            self.contact_page.submit_button_click()
            self.functions.WaitLocate(Locator.YANDEX_PAGE)
            self.functions.getScreenshot("form_sent")


    @pytest.mark.sanity
    @allure.title("Required_fields")
    @allure.severity("Minor")
    def test_required_fields(self):
        with allure.step("Checking required fields on contact form"):
            self.contact_page.submit_button_click()
            self.functions.WaitLocate(Locator.R_FIELD)
            self.functions.getScreenshot("req_fields")


    @pytest.mark.sanity
    @allure.title("Name field checking")
    @allure.severity("Minor")
    def test_name_field(self):

        with allure.step("Checking Name field"):
            self.contact_page.name_field_send_text("         ")

        with allure.step("Enter the remaining fields"):
            self.contact_page.email_field_send_text("random@mail.com")
            self.contact_page.phone_field_send_text("8999999999999")
            self.contact_page.comment_field_send_text("Hello test")

        with allure.step("Send incorrect form"):
            self.contact_page.submit_button_click()

        with allure.step("Checking name field again"):
            self.functions.WaitLocate(Locator.R_FIELD)
            self.functions.ElementSelection(Locator.R_FIELD)

        with allure.step("Take screenshot"):
            self.functions.getScreenshot("invalid_name")


    @pytest.mark.sanity
    @allure.title("Phone field checking")
    @allure.severity("Minor")
    def test_phone_field(self):

        with allure.step("Checking Phone field"):
            self.contact_page.phone_field_send_text("899999")

        with allure.step("Enter the remaining fields"):
            self.contact_page.email_field_send_text("random@mail.com")
            self.contact_page.name_field_send_text("Hello")
            self.contact_page.comment_field_send_text("Hello test")

        with allure.step("Send incorrect form"):
            self.contact_page.submit_button_click()

        with allure.step("Checking name field again"):
            self.functions.WaitLocate(Locator.INVALID_NUMBER)
            self.functions.ElementSelection(Locator.INVALID_NUMBER)

        with allure.step("Take screenshot"):
            self.functions.getScreenshot("invalid_nimber")


    # @pytest.mark.smoke
    # @pytest.mark.sanity
    # @allure.title("Social links checking")
    # @allure.severity("Critical")
    # def test_social_link(self):
    #     with allure.step("Checking rss link"):
    #         self.contact_page.rss_link_checking()
    #     with allure.step("Checking youtube link"):
    #         self.contact_page.youtube_link_checking()
    #     with allure.step("Checking facebook link"):
    #         self.contact_page.facebook_link_checking()
    #     with allure.step("Checking twitter link"):
    #         self.contact_page.twitter_link_checking()



