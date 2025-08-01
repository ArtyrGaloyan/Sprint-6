
import allure

from ..urls.urls import URLS
from ..pages.header_page import HeaderPage
from ..locators.dzen import DzenLocator


class TestRedirectHeader:
    "Тест кейс кнопок в header"

    @allure.title("""Тест: проверка перенаправление на dzen,
                после нажатия на логотип Yandex""")
    def test_click_logo_yandex_redirect_home_page_ya(self, browser_def):
        header = HeaderPage(browser_def)
        header.open_url(URLS['home'])
        header.click_yandex_logo()
        header.change_the_window(1)
        header.get_element(DzenLocator.search)
        current_url = header.current_url()
        assert URLS["dzen"] in current_url

    @allure.title("""Тест: проверка перенаправления на главную страницу,
                после нажатия на логотип Самокат""")
    def test_click_logo_scooter_redirect_home_page_scooter(self, browser_def):
        header = HeaderPage(browser_def)
        header.open_url(URLS['home'])
        header.click_order()
        header.click_scooter_logo()
        current_url = header.current_url()
        assert current_url in URLS['home']
