import selenium
import allure
import pytest

from data import Data
from locators import Locator
from functions import Functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Links import Links

#########################################################################################
# В данном классе мы создаем страницу, __init__ которой будет подтягиваться во все pages
# А так же пишем общие функции, но лучше писать в файл functions.py
#########################################################################################
class BasePage():

#######################################################
# Тут обьявляем общие параметры для тестов
#######################################################
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(30) # Обьявляем ожидания для страниц
        # self.driver.set_window_size(1920, 1080) # Указываем размер окна
        self.driver.maximize_window() # Указываем размер окна
        self.wait = WebDriverWait(self.driver, 30) # Указываем ожидания для элементов
        self.functions = Functions(self.driver) # Создаем обьект для того чтобы использовать функции в pages

#######################################################
# Тут обьявляем все константы, локаторы, ссылки, данные
#######################################################
        self.links = Links()
        self.Locator = Locator()
        self.data = Data()

    def open_link(self, link):
        return self.driver.get(link)

    def wait_clicable(self, elem):
        self.wait.until(EC.element_to_be_clickable((elem)))