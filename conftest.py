import pytest

from selenium import webdriver


@pytest.fixture(scope='function')
def browser_def():
    "Браузер для функции"
    options = webdriver.FirefoxOptions()
    options.add_argument("--private")
    browser = webdriver.Firefox(options=options)
    yield browser
    browser.quit()
