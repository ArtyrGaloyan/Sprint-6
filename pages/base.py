import platform
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException, NoSuchElementException
)
import allure

OS = platform.system()
TIME_MAX = 10


class BasePage:
    def __init__(self, browser):
        self.__browser = browser
        self.__wait = WebDriverWait(browser, TIME_MAX)

    def __define_os(self, field):
        if OS == "Windows" or OS == "Linux":
            self.__clean_win_uix(field)
        if OS == "Darwin":
            self.__clean_mac_os(field)

    def __clean_mac_os(self, field):
        field.send_keys(Keys.COMMAND + "a")
        field.send_keys(Keys.DELETE)

    def __clean_win_uix(self, field):
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)

    @allure.step("Очистка поля")
    def clear_field(self, field):
        self.__define_os(field)

    @allure.step("Прокрутка до элемента")
    def scrol_to_element(self, element):
        self.__browser.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ожидание получения элемента")
    def get_element(self, path):
        return self.__wait.until(EC.presence_of_element_located(path))

    @allure.step("Ожидание получения кнопки и нажатия")
    def get_button_click(self, path=None, element=None):
        if element is None:
            element = self.get_element(path)
        self.__wait.until(EC.element_to_be_clickable(element))
        element.click()
        return element

    @allure.step("Открытие url")
    def open_url(self, url):
        self.__browser.get(url)

    @allure.step("Получаем текущий url")
    def current_url(self):
        return self.__browser.current_url

    @allure.step("Меняем активную вкладку браузера")
    def change_the_window(self, number_window):
        new_window = self.__browser.window_handles[number_window]
        self.__browser.switch_to.window(new_window)