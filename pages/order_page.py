from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_locators import OrderLocators


class OrderPageObject:
    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element(*OrderLocators.NAME_FIELD).send_keys(name)

    def set_last_name(self, last_name):
        self.driver.find_element(*OrderLocators.LAST_NAME_FIELD).send_keys(last_name)

    def set_address(self, address):
        self.driver.find_element(*OrderLocators.ADDRESS_FIELD).send_keys(address)

    def set_phone(self, phone):
        self.driver.find_element(*OrderLocators.PHONE_FIELD).send_keys(phone)

    def continue_button_click(self):
        self.driver.find_element(*OrderLocators.CONTINUE_BUTTON).click()

    def set_metro_station(self):
        self.driver.find_element(*OrderLocators.METRO_STATION_FIELD).click()
        (WebDriverWait(self.driver, 10)).until(
            expected_conditions.presence_of_element_located(OrderLocators.METRO_BUTTON))
        self.driver.find_element(*OrderLocators.METRO_BUTTON).click()

    def set_date(self, date):
        date_field_element = self.driver.find_element(*OrderLocators.DATE_FIELD)
        date_field_element.send_keys(date)
        date_field_element.send_keys(Keys.ENTER)

    def set_rental_period(self):
        self.driver.find_element(*OrderLocators.RENTAL_PERIOD_FIELD).click()
        (WebDriverWait(self.driver, 10)).until(
            expected_conditions.presence_of_element_located(OrderLocators.RENTAL_PERIOD_OPTION))
        self.driver.find_element(*OrderLocators.RENTAL_PERIOD_OPTION).click()

    def order_button_click(self):
        self.driver.find_element(*OrderLocators.ORDER_BUTTON).click()

    def confirm_order_creation_button_click(self):
        (WebDriverWait(self.driver, 10)).until(
            expected_conditions.presence_of_element_located(OrderLocators.CONFIRM_ORDER_CREATION_BUTTON))
        self.driver.find_element(*OrderLocators.CONFIRM_ORDER_CREATION_BUTTON).click()

    def is_order_created_modal_header_visible(self):
        return self.driver.find_element(*OrderLocators.ORDER_CREATED_MODAL_HEADER).is_displayed()

    def fill(self, name, last_name, address, phone, date):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro_station()
        self.set_phone(phone)
        self.continue_button_click()
        self.set_date(date)
        self.set_rental_period()
