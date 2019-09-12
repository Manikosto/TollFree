__author__ = 'Alexey Koledachkin'

import unittest
import allure
import pytest
import selenium
import time
from xml.etree.ElementTree import fromstring
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))





class EnvironmentSetup(unittest.TestCase):

    #setUP contains the browser setup attributes

    def setUp(self):

        with open('../allure-results/environment.xml', 'r') as env:
            root = fromstring(env.read())
            browser = root.find("./parameter/value[1]")

        if browser.text == 'Chrome':
            self.driver = webdriver.Chrome("../Drivers/chromedriver.exe")

        elif browser.text == 'Edge':
            self.driver = webdriver.Edge("../Drivers/MicrosoftWebDriver.exe")

        elif browser.text == 'Firefox':
            self.driver = webdriver.Firefox(executable_path="../Drivers/geckodriver.exe")

        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 30)


#tearDown method just to close all the browser instances and then quit

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.close()
        self.driver.quit()

