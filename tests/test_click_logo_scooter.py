from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.url_locators import UrlLocators
from pages.home_page import HomePageObject


def test_click_logo_scooter(open_order):
    driver = open_order
    home = HomePageObject(driver)
    home.click_logo_scooter()
    assert WebDriverWait(driver, 15).until(expected_conditions.url_to_be(UrlLocators.HOME_PAGE))

