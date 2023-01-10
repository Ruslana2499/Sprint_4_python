from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.url_locators import UrlLocators
from pages.home_page import HomePageObject


def test_click_logo_yandex(open_home):
    driver = open_home
    home = HomePageObject(driver)
    home.click_logo_yandex()
    home.switch_to_window(1)
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(UrlLocators.YANDEX_HOME_PAGE))
    assert driver.current_url == UrlLocators.YANDEX_HOME_PAGE

