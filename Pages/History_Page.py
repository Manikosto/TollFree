import selenium
import allure
import pytest
import time
from data import Data
from locators import Locator
from functions import Functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Pages.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class History(BasePage):

    START_DATE = (By.XPATH, Locator.START_DATE)
    END_DATE = (By.XPATH, Locator.END_DATE)
    TYPE_CONFERENCE = (By.XPATH, Locator.TYPE_CONFERENCE) # Select
    SEARCH = (By.XPATH, Locator.SEARCH)

    ### Sorting
    SORT_BY_DATE_TIME = (By.XPATH, Locator.SORT_BY_DATE_TIME)
    SORT_BY_END_TIME = (By.XPATH, Locator.SORT_BY_END_TIME)

    SORT_BY_CALLERS = (By.XPATH, Locator.SORT_BY_CALLERS)
    SORT_BY_DURATION = (By.XPATH, Locator.SORT_BY_DURATION)
    SORT_BY_RECORDING_OPTIONS = (By.XPATH, Locator.SORT_BY_RECORDING_OPTIONS)
    SORT_BY_SIZE = (By.XPATH, Locator.SORT_BY_SIZE)

    ### Work with table
    OPEN_RECORDING = (By.XPATH, Locator.OPEN_RECORDING)

    DOWNLOAD_PDF = (By.XPATH, Locator.DOWNLOAD_PDF)
    DOWNLOAD = (By.XPATH, Locator.DOWNLOAD)
    PLAY = (By.XPATH, Locator.PLAY)
    TRASH = (By.XPATH, Locator.TRASH)
    CLOSE_RECORDING = (By.XPATH, Locator.CLOSE_RECORDING)


    # def open_recording(self):
    #     open_recording = self.driver.find_element(*self.OPEN_RECORDING)
    #     open_recording.click()
    #     assert open_recording.get_attribute("class") == "fa fa-minus icon-minus"

    def play_recording(self):
        self.driver.find_element(*self.PLAY).click()
        time.sleep(1)
        self.functions.getScroll("300")
        time.sleep(1)

    def assert_of_recording_work(self):
            self.functions.WaitLocate(Locator.PAUSE)
            time.sleep(10)

    def click_on_pause_button(self):
        self.driver.find_element(By.XPATH, Locator.PAUSE).click()
        self.functions.WaitLocate(Locator.PLAY_BUTTON)

    def click_on_stop_button(self):
        self.driver.find_element(By.XPATH, Locator.STOP).click()
        assert self.driver.find_element(By.XPATH, Locator.CURRENT_TIME).text == "00:00"

    def click_on_mute_button(self):
        self.functions.getClick(Locator.MUTE)
        self.functions.WaitLocate(Locator.UNMUTE)

    def click_on_unmute_button(self):
        self.functions.getClick(Locator.UNMUTE)
        self.functions.WaitLocate(Locator.MUTE)

    def click_on_repeat_button(self):
        self.driver.find_element(By.XPATH, Locator.REPEAT).click()
        self.functions.WaitLocate(Locator.REPEAT_OFF)

    def click_on_repeat_off_button(self):
        self.driver.find_element(By.XPATH, Locator.REPEAT_OFF).click()
        self.functions.WaitLocate(Locator.REPEAT)

    def click_on_download_pdf_button(self):
        self.driver.find_element(*self.DOWNLOAD_PDF).click()
        time.sleep(3)
        self.driver.switch_to.window(window_name=self.driver.window_handles[1])
        self.functions.getScreenshot("Download PDF")
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
        self.driver.switch_to.window(window_name=self.driver.window_handles[0])

    def close_recording(self):
        self.driver.find_element(*self.CLOSE_RECORDING).click()

    def enter_start_date(self):
        self.driver.find_element(*self.START_DATE).send_keys(Data.START_DATE)

    def enter_end_date(self):
        self.driver.find_element(*self.END_DATE).send_keys(Data.END_DATE)

    def click_on_search_button(self):
        self.driver.find_element(*self.SEARCH).click()

