import pytest as pytest
# импортировали пакет Selenium WebDriver
from selenium import webdriver

from locators.url_locators import UrlLocators
from pages.home_page import HomePageObject


@pytest.fixture
def create_driver_instance():
    driver = webdriver.Firefox()
    driver.set_window_size(1280, 1024)
    return driver


@pytest.fixture
def open_home(create_driver_instance):
    # открыть страницу
    driver = create_driver_instance
    driver.get(UrlLocators.HOME_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def open_order(create_driver_instance):
    # открыть страницу
    driver = create_driver_instance
    driver.get(UrlLocators.ORDER_PAGE)
    yield driver
    driver.quit()

@pytest.fixture
def prepare_home_page(open_home):
    driver = open_home
    home = HomePageObject(driver)
    home.click_accept_cookies_button()
    return home
