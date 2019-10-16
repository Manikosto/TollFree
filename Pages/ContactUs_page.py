import selenium
import allure
import pytest

from data import Data
from locators import Locator
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ContactUs(BasePage):

    NAME = (By.XPATH, Locator.NAME)
    EMAIL = (By.XPATH, Locator.EMAIL)
    PHONE = (By.XPATH, Locator.PHONE)
    COMMENTS = (By.XPATH, Locator.COMMENTS)
    SUBMIT = (By.XPATH, Locator.SUBMIT)

    LOGO = (By.XPATH, Locator.LOGO)
    SIGN_UP = (By.XPATH, Locator.SIGN_UP)
    LOGIN = (By.XPATH, Locator.LOGIN)
    HOME = (By.XPATH, Locator.HOME)
    CONTACT_US = (By.XPATH, Locator.CONTACT_US)
    FAQ = (By.XPATH, Locator.FAQ)
    ABOUT_US = (By.XPATH, Locator.ABOUT_US)
    HOME_BUTTON = (By.XPATH, Locator.HOME_BUTTON)
    CONTACT_BOTTOM = (By.XPATH, Locator.CONTACT_BOTTOM)
    FAQ_BOTTOM = (By.XPATH, Locator.FAQ_BOTTOM)
    ABOUT_BOTTOM = (By.XPATH, Locator.ABOUT_BOTTOM)
    POP_UP = (By.XPATH, Locator.POP_UP)

    RSS = (By.XPATH, Locator.RSS)
    FACEBOOK = (By.XPATH, Locator.FACEBOOK)
    YOUTUBE = (By.XPATH, Locator.YOUTUBE)
    TWITTER = (By.XPATH, Locator.TWITTER)



    def submit_button_click(self):
        self.driver.find_element(*self.SUBMIT).click()

    def name_field_send_text(self,text):
        return self.driver.find_element(*self.NAME).send_keys(text)

    def email_field_send_text(self,text):
            return self.driver.find_element(*self.EMAIL).send_keys(text)

    def phone_field_send_text(self,text):
            return self.driver.find_element(*self.PHONE).send_keys(text)

    def comment_field_send_text(self,text):
            return self.driver.find_element(*self.COMMENTS).send_keys(text)

    def send_form(self, name, email, phone, comment):
        self.name_field_send_text(name)
        self.email_field_send_text(email)
        self.phone_field_send_text(phone)
        self.comment_field_send_text(comment)

    def rss_link_checking(self):
        self.driver.find_element(*self.RSS).click()
        # Вставить валидацию тайтла
        self.functions.getScreenshot("rss_page")
        self.driver.back()

    def youtube_link_checking(self):
        self.driver.find_element(*self.YOUTUBE).click()
        # Вставить валидацию тайтла
        self.functions.getScreenshot("youtube_page")
        self.driver.back()

    def facebook_link_checking(self):
        self.driver.find_element(*self.FACEBOOK).click()
        # Вставить валидацию тайтла
        self.functions.getScreenshot("facebook_page")
        self.driver.back()

    def twitter_link_checking(self):
        self.driver.find_element(*self.TWITTER).click()
        # Вставить валидацию тайтла
        self.functions.getScreenshot("twitter_page")
        self.driver.back()
