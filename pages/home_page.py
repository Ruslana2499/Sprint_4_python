from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.home_locators import HomeLocators


class HomePageObject:
    def __init__(self, driver):
        self.driver = driver

    def get_drop_down_list_item_id(self, item):
        button_id = item.get_attribute("id")
        return button_id[button_id.index("-") + 1:]

    def get_drop_down_list_ids(self):
        result = []
        buttons = self.driver.find_elements(*HomeLocators.DROP_DOWN_LIST_ITEM)
        for button in buttons:
            button_id = self.get_drop_down_list_item_id(button)
            result.append(button_id)
        return result

    def click_drop_down_list_item(self, id):
        buttons = self.driver.find_elements(*HomeLocators.DROP_DOWN_LIST_ITEM)
        for button in buttons:
            button_id = self.get_drop_down_list_item_id(button)
            if button_id == id:
                WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(button))
                button.click()
                break

    def get_visible_drop_down_list_text_block_id(self):
        panels = self.driver.find_elements(*HomeLocators.DROP_DOWN_LIST_TEXT)
        for panel in panels:
            if panel.is_displayed():
                return self.get_drop_down_list_item_id(panel)
        return None

    def click_order_button_in_header(self):
        self.driver.find_element(*HomeLocators.ORDER_BUTTON_IN_HEADER).click()

    def click_order_button_in_body(self):
        self.driver.find_element(*HomeLocators.ORDER_BUTTON_IN_BODY).click()

    def click_accept_cookies_button(self):
        self.driver.find_element(*HomeLocators.ACCEPT_COOKIES_BUTTON).click()

    def click_logo_scooter(self):
        self.driver.find_element(*HomeLocators.SCOOTER_LOGO).click()

    def click_logo_yandex(self):
        self.driver.find_element(*HomeLocators.YANDEX_LOGO).click()

    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])
