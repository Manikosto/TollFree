__author__ = 'Alexey Koledachkin'

import allure
import time
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


from selenium.webdriver.common.keys import Keys
from TestBase.EnvironmentSetUp import EnvironmentSetup
from selenium.webdriver.common.by import By
from locators import Locator
from Data import Data
from TestBase.Functions import Functions
from Pages.LoginPage import Login
from Pages.HistoryRecording import History
from TestBase.Links import Links

@allure.parent_suite("History and Recording tests")
class HistoryRecording(EnvironmentSetup):

###   INIT   ###

    def INIT(self):
        driver = self.driver

        ### Announce of locators
        self.locator = Locator()
        self.data = Data()

        ### Announce objects
        self.history = History(driver)
        self.function = Functions(driver)


    @allure.suite("Player")
    @allure.title("Player testing")
    @allure.description("Checking player working")
    @allure.severity("Critical")
    def test_CheckingPlayer(self):
        with allure.step("Opening page and logining"):
            self.INIT()

        with allure.step("Checking title"):
            self.function.TitleCheck(Locator.recordings)

        with allure.step("Open recording"):
            self.history.open_recording.click()


        with allure.step("Checking correct opening of record"):
            assert self.history.open_recording.get_attribute("class") == "fa fa-minus icon-minus"
            self.function.getScreenshot("openrecord")

        with allure.step("Play recording"):
            time.sleep(2)
            self.history.play.click()
            self.function.getScreenshot("open")
            self.function.getScroll("310")

        with allure.step("Assert that recording work"):
            self.function.WaitLocate(Locator.pause)
            time.sleep(10)
            self.function.getScreenshot("playingRec")

        with allure.step("Click by Pause button"):
            self.driver.find_element(By.XPATH, Locator.pause).click()
            self.function.WaitLocate(Locator.play_button)
            self.function.getScreenshot("Pause button")

        with allure.step("Click by Stop button"):
            self.driver.find_element(By.XPATH, Locator.stop).click()
            assert self.driver.find_element(By.XPATH, Locator.current_time).text == "00:00"
            self.function.getScreenshot("Stop button")

        with allure.step("Click by Mute button"):
            self.function.getClick(Locator.mute)
            self.function.WaitLocate(Locator.unmute)
            self.function.getScreenshot("Mute button")

        with allure.step("Click by Unmute button"):
            self.function.getClick(Locator.unmute)
            self.function.WaitLocate(Locator.mute)
            self.function.getScreenshot("Unmute button")

        with allure.step("Click by repeat button"):
            self.driver.find_element(By.XPATH, Locator.repeat).click()
            self.function.WaitLocate(Locator.repeat_off)
            self.function.getScreenshot("repeat button")

        with allure.step("Click by repeat off button"):
            self.driver.find_element(By.XPATH, Locator.repeat_off).click()
            self.function.WaitLocate(Locator.repeat)
            self.function.getScreenshot("repeatoff button")

        with allure.step("Download PDF click"):
            self.driver.find_element(By.XPATH, Locator.download_pdf).click()
            time.sleep(3)
            self.driver.switch_to.window(window_name=self.driver.window_handles[1])
            self.function.getScreenshot("Download PDF")
            self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
            self.driver.switch_to.window(window_name=self.driver.window_handles[0])

        # with allure.step("Download mp3"):
        #     self.driver.find_element(By.XPATH, Locator.download).click()


        with allure.step("Close Recording"):
            self.driver.find_element(By.XPATH, Locator.close_recording).click()
            self.driver.find_element(By.XPATH, Locator.close_recording).click()
            self.function.getScreenshot("closerecord")





    @allure.suite("Filtering")
    @allure.title("Positive filtering by date")
    @allure.description("")
    @allure.severity("Critical")
    @allure.link(name = "Positive filtering", url = "https://testlink.int/linkto.php?tprojectPrefix=STF&item=testcase&id=STF-28")
    def test_PositiveFilteringByDate(self):
        with allure.step("Opening page and logining"):
            self.INIT()
        with allure.step("Checking title"):
            self.function.TitleCheck(Locator.recordings)

        with allure.step("Enter start date"):
            self.history.start_date.send_keys(Data.start_date)

        with allure.step("Enter end date"):
            self.history.end_date.send_keys(Data.end_date)

        with allure.step("Search click"):
            self.history.search.click()
            self.function.WaitLocate(Locator.open_recording)
            self.function.getScreenshot("allconference")


    # @allure.suite("History and Recordings")
    # @allure.title("Negative filtering by date")
    # @allure.description("")
    # @allure.severity("Critical")
    # def test_NegativeFilteringByDate(self):
    #     with allure.step("Opening page and logining"):
    #         self.INIT()
    #     with allure.step("Checking title"):
    #         self.function.TitleCheck(Locator.recordings)
    #
    #     with allure.step("Enter start date"):
    #         self.history.start_date.send_keys(Data.end_date)
    #
    #     with allure.step("Enter end date"):
    #         self.history.end_date.send_keys(Data.start_date)
    #
    #     with allure.step("Search click"):
    #         self.history.search.click()
    #         self.function.WaitLocate(Locator.open_recording)
    #         self.function.getScreenshot("allconference")


    # @allure.parent_suite("Основной сьют")
    # @allure.title("Positive filtering by date")
    # @allure.description("")
    # @allure.severity("Critical")
    # def test_PositiveFilteringByDate(self):
    #     with allure.step("Opening page and logining"):
    #         self.INIT()
    #     with allure.step("Checking title"):
    #         self.function.TitleCheck(Locator.recordings)
    #
    #     with allure.step("Enter start date"):
    #         self.history.start_date.send_keys(Data.start_date)
    #
    #     with allure.step("Enter end date"):
    #         self.history.end_date.send_keys(Data.end_date)
    #
    #     with allure.step("Search click"):
    #         self.history.search.click()
    #         self.function.WaitLocate(Locator.open_recording)
    #         self.function.getScreenshot("allconference")