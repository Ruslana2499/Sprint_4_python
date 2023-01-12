from selenium.webdriver.common.by import By


class OrderLocators:
    NAME_FIELD = By.CSS_SELECTOR, "input[placeholder*='Имя']"
    LAST_NAME_FIELD = By.CSS_SELECTOR, "input[placeholder*='Фамилия']"
    ADDRESS_FIELD = By.CSS_SELECTOR, "input[placeholder*='Адрес']"
    METRO_STATION_FIELD = By.CSS_SELECTOR, "input[placeholder*='метро']"
    METRO_BUTTON = By.CSS_SELECTOR, ".select-search__option"
    PHONE_FIELD = By.CSS_SELECTOR, "input[placeholder*='Телефон']"
    DATE_FIELD = By.CSS_SELECTOR, "input[placeholder*='Когда привезти самокат']"
    RENTAL_PERIOD_FIELD = By.CLASS_NAME, "Dropdown-control"
    RENTAL_PERIOD_OPTION = By.CLASS_NAME, "Dropdown-option"
    CONTINUE_BUTTON = By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM"
    ORDER_BUTTON = By.XPATH, ".//*[text()='Заказать' and contains(@class,'Button_Middle__1CSJM')]"
    CONFIRM_ORDER_CREATION_BUTTON = By.XPATH, ".//*[text()='Да']"
    ORDER_CREATED_MODAL_HEADER = By.XPATH, ".//*[text()='Заказ оформлен']"
