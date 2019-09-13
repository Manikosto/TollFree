__author__ = 'Alexey Koledachkin'

import unittest
import allure
import pytest
import selenium
import time
from xml.etree.ElementTree import fromstring
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from TestBase.Links import Links
from locators import Locator
from Data import Data
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))





class EnvironmentSetup(unittest.TestCase):

#################################################################################################
#                                WE ANNOUNCE ENVIRONMENT HERE                                   #
#################################################################################################
    def setUp(self): # Pre-condition for all tests
        with open('../allure-results/environment.xml', 'r') as env:
            root = fromstring(env.read())
            browser = root.find("./parameter/value[1]") # Search browser value
        if browser.text == 'Chrome': # Run in Chrome
            self.driver = webdriver.Chrome("../Drivers/chromedriver.exe")
        elif browser.text == 'Edge': # Run in Edge
            self.driver = webdriver.Edge("../Drivers/MicrosoftWebDriver.exe")
        elif browser.text == 'Firefox': # Run in Firefox
            self.driver = webdriver.Firefox(executable_path="../Drivers/geckodriver.exe")

#################################################################################################
#                                WE ANNOUNCE DYNAMIC DATA HERE                                  #
#################################################################################################
        with open('../allure-results/environment.xml', 'r') as env:
            root = fromstring(env.read())
            browser = root.find("./parameter[3]/value") # Search Stand value

#################################################################################################
#                                WE ANNOUNCE QA DATA HERE                                       #
#################################################################################################
        if browser.text == 'QA':

#################################################################################################
#                                WE ANNOUNCE DATA FOR LOGIN HERE                                #
#################################################################################################
            Data.correct_dial = "(775) 360-1641"  # Write here toll-free number from account
            Data.correct_access = "531144"  # Write here access code from account
            Data.correct_pin = "6910"  # Write here PIN from account
            Data.Toll_number = "(775) 360-1642" # Write here Toll number from account
            Data.Playback_number = "(775) 360-1643" # Write here Playback number from account


#################################################################################################
#                             WE ANNOUNCE DATA FOR ALL PAGE LINKS                               #
#################################################################################################
            Links.account = "https://qa-www.simpletollfree.com/login"
            Links.contact_us = "https://qa-www.simpletollfree.com/contact-us"
            Links.home = "https://qa-www.simpletollfree.com"
            Links.login = "https://qa-www.simpletollfree.com/login"
            Links.sign_up = "https://qa-www.simpletollfree.com/signup?marketing_tag=qa_test_Le8KzIP57Nf00Hbb"
            Links.faq = "https://qa-www.simpletollfree.com/faq"
            Links.recordings = "https://qa-www.simpletollfree.com/recordings"

#################################################################################################
#                              WE ANNOUNCE LETTER TITLE FOR CHECKING                            #
#################################################################################################
            Data.registration_letter_title = "//span[text()='QA MODE:SimpleTollFree.com Account Registration']"





#################################################################################################
#                                WE ANNOUNCE PRODUCTION DATA HERE                                  #
#################################################################################################
        elif browser.text == 'Production':

            Data.Toll_number = "(951) 262-1555"
            Data.Playback_number = "(951) 262-1999"

            ### Data for login ###
            Data.correct_dial = "(877) 216-1555"  # Write here your toll-free number
            Data.correct_access = "661400"  # Write here your access code
            Data.correct_pin = "1756"  # Write here your PIN

#################################################################################################
#                             WE ANNOUNCE DATA FOR ALL PAGE LINKS                               #
#################################################################################################
            Links.account = "https://www.simpletollfree.com/login"
            Links.contact_us = "https://www.simpletollfree.com/contact-us"
            Links.home = "https://www.simpletollfree.com"
            Links.login = "https://www.simpletollfree.com/login"
            Links.sign_up = "https://www.simpletollfree.com/signup?marketing_tag=qa_test_Le8KzIP57Nf00Hbb"
            Links.faq = "https://www.simpletollfree.com/faq"
            Links.recordings = "https://www.simpletollfree.com/recordings"





        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 30)


#tearDown method just to close all the browser instances and then quit

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.close()
        self.driver.quit()

