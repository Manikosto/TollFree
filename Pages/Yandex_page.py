__author__ = 'Alexey Koledachkin'

import unittest
import allure
import pytest
import selenium
import time
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from selenium.webdriver.common.by import By
from locators import Locator
from data import Data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Pages.BasePage import BasePage

# driver.find_element(By.XPATH(''))
class YandexLogin(BasePage):



    def Autorization(self, login, password):
        self.driver.get("https://passport.yandex.ru/auth?from=mail&origin=hostroot_homer_auth_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1")
        self.driver.find_element(By.XPATH, Locator.TEST_LOGIN_EMAIL).send_keys(login)
        self.driver.find_element(By.XPATH, Locator.TEST_SUBMIT_BUTTON).click()
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, Locator.TEST_PASSWORD_EMAIL)))
            self.driver.find_element(By.XPATH, Locator.TEST_PASSWORD_EMAIL).send_keys(password)
            self.driver.find_element(By.XPATH, Locator.TEST_SUBMIT_BUTTON).click()
        except:
            pass

    def CheckLetter(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, Data.registration_letter_title)))
            self.driver.find_element(By.XPATH, Data.registration_letter_title).click()
            self.pin_letter = self.driver.find_element(By.XPATH, Locator.PIN_LETTER)
            self.pin_letter = self.pin_letter.text

        except:
            pass

    def EmptyEmail(self):
        self.driver.back()
        self.driver.find_element(By.XPATH, Locator.CHECKBOX_CLEAR).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, Locator.DELETE)))
        self.driver.find_element(By.XPATH, Locator.DELETE).click()









