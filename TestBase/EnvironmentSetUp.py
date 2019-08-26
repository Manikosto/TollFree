__author__ = 'Alexey Koledachkin'

import unittest
import allure
import pytest
import selenium
import time
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

class EnvironmentSetup(unittest.TestCase):

    #setUP contains the browser setup attributes
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome("../Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window() 
        cls.wait = WebDriverWait(cls.driver, 30)


#tearDown method just to close all the browser instances and then quit
    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()

