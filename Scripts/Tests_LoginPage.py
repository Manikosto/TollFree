__author__ = 'Alexey Koledachkin'

import allure
import time
import sys
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from TestBase.EnvironmentSetUp import EnvironmentSetup
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from locators import Locator
from TestBase.Functions import Functions
from Pages.LoginPage import Login
from TestBase.Links import Links
from Data import Data

@allure.parent_suite("Login page tests")
class LoginPage(EnvironmentSetup):

###   INIT   ###

    def INIT(self):
        driver = self.driver
        self.driver.get(Links.login)
        self.function = Functions(driver)
        self.login = Login(driver)
        self.locator = Locator()

###   Tests   ###

    # Requaired fields

    @allure.suite("Login")
    @allure.title("Correct login")
    @allure.description("Open Login page and login on site")
    @allure.severity("Critical")
    def test_Login(self):
        # Open page in the browser
        with allure.step("Open page in the browser"):
            self.INIT()
        # Title cheking
        with allure.step("Title cheking"):
            self.function.TitleCheck("Login - SimpleTollFree")
        with allure.step("Enter correct data"):
            self.login.dial_number.send_keys("998377")
            self.login.accesscode.send_keys(Data.correct_access)
            self.login.host_pin.send_keys(Data.correct_pin)
        with allure.step("Remember me"):
            self.login.remember_me.click()
        with allure.step("Login"):
            self.login.submit.click()
        with allure.step("Wait login page"):
            self.function.WaitLocate(Locator.page_name)
            self.function.getScreenshot("login")
        with allure.step("Title cheking"):
            self.function.TitleCheck(Locator.login_title)




# Forgot link
#     @allure.suite("Login")
#     @allure.title("Forgot password link")
#     @allure.description("Open Login page and login on site")
#     @allure.severity("Critical")
#     def test_ForgotPassword(self):
#         # Open page in the browser
#         with allure.step("Open page in the browser"):
#             self.INIT()
#         # Title cheking
#         with allure.step("Title cheking"):
#             self.function.TitleCheck("Login - SimpleTollFree")
#         # CLick on forgot password link
#         time.sleep(3)
#         with allure.step("Go to forgot password link"):
#             self.function.getClick(Locator.forgot_pass)
#             time.sleep(3)
#             self.login.send_info.click()
#         time.sleep(3)
#         # Enter data
#         with allure.step("Enter data"):
#
#             self.wait.until(EC.presence_of_element_located((By.XPATH, Data.correct_access)))
#             self.driver.execute_script("arguments[0].click();", Data.correct_access)
#             self.login.accesscode.send_keys(Data.correct_access)
        # # Send info
        # with allure.step("Send info"):
        #     self.login.send_info.click()
        #
        # with allure.step(""):
        #     self.function.WaitLocate(self.locator.alert)
        #     self.function.getScreenshot("forgot_pass")
