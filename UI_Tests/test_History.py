import pytest
import allure
import time
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from Links import Links
from locators import Locator
from functions import Functions
from Pages.Login_page import LoginPage
from Pages.History_Page import History
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("choose_stand")
@allure.parent_suite("History and Recordings page")
@allure.suite("History and Recordings page")
class Test_History():

    def setup(self):
        self.links = Links()
        self.locators = Locator()
        self.functions = Functions(self.driver)
        self.login_page = LoginPage(self.driver)
        self.history_page = History(self.driver)

        self.driver.get(self.links.login)
        self.login_page.login_in_account()
        self.driver.get(Links.recordings)

    @pytest.mark.smoke
    @pytest.mark.sanity
    @allure.title("Player checking")
    @allure.severity("Critical")
    @pytest.mark.pop
    def test_player_checking(self):

        # with allure.step("Opening recording"):
        #     self.history_page.open_recording()
        #     self.functions.getScreenshot("open_recording")

        with allure.step("Opening recording"):
            self.history_page.play_recording()
            self.functions.getScreenshot("play_screenshot")

        with allure.step("Assertion of recording work"):
            self.history_page.assert_of_recording_work()
            self.functions.getScreenshot("playingRec")

        with allure.step("Click on pause button"):
            self.history_page.click_on_pause_button()
            self.functions.getScreenshot("Pause_button")

        with allure.step("Click on stop button"):
            self.history_page.click_on_stop_button()
            self.functions.getScreenshot("click_on_stop_button")

        with allure.step("Click on mute button"):
            self.history_page.click_on_mute_button()
            self.functions.getScreenshot("click_on_mute_button")

        with allure.step("Click on unmute button"):
            self.history_page.click_on_unmute_button()
            self.functions.getScreenshot("click_on_unmute_button")

        with allure.step("Click on repeat button"):
            self.history_page.click_on_repeat_button()
            self.functions.getScreenshot("click_on_repeat_button")

        with allure.step("Click on repeat off button"):
            self.history_page.click_on_repeat_off_button()
            self.functions.getScreenshot("click_on_repeat_off_button")

        with allure.step("Click on download pdf button"):
            self.history_page.click_on_download_pdf_button()

        with allure.step("Close recording"):
            self.history_page.close_recording()



    @pytest.mark.smoke
    @pytest.mark.sanity
    @allure.title("Positive filtering")
    @allure.severity("Critical")
    def test_positive_filtering(self):

        with allure.step("Enter start date"):
            self.history_page.enter_start_date()

        with allure.step("Enter end date"):
            self.history_page.enter_end_date()

        with allure.step("Click on search button"):
            self.history_page.click_on_search_button()

        with allure.step("Wait for opening recording"):
            self.functions.WaitLocate(Locator.OPEN_RECORDING)








