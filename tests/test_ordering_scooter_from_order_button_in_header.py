from pages.home_page import HomePageObject
from pages.order_page import OrderPageObject


def test_ordering_scooter_from_order_button_in_header(open_home):
    driver = open_home
    home = HomePageObject(driver)
    home.click_order_button_in_header()
    order = OrderPageObject(driver)
    order.fill("йцуке", "йцуке", "йцуке", "11111111111", "27.12.2022")
    order.order_button_click()
    order.confirm_order_creation_button_click()
    assert order.is_order_created_modal_header_visible()


def test_ordering_scooter_from_order_button_in_body(open_home):
    driver = open_home
    home = HomePageObject(driver)
    home.click_accept_cookies_button()
    home.click_order_button_in_body()
    order = OrderPageObject(driver)
    order.fill("йцуке", "йцуке", "йцуке", "11111111111", "27.12.2022")
    order.order_button_click()
    order.confirm_order_creation_button_click()
    assert order.is_order_created_modal_header_visible()
