from selenium.webdriver.common.by import By


class HomeLocators:
    DROP_DOWN_LIST_ITEM = By.CLASS_NAME, "accordion__button"
    DROP_DOWN_LIST_TEXT = By.CLASS_NAME, "accordion__panel"
    ORDER_BUTTON_IN_HEADER = By.CSS_SELECTOR, ".Header_Header__214zg .Button_Button__ra12g"
    ORDER_BUTTON_IN_BODY = By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM"
    ACCEPT_COOKIES_BUTTON = By.CLASS_NAME, "App_CookieButton__3cvqF"
    YANDEX_LOGO = By.CLASS_NAME, "Header_LogoYandex__3TSOI"
    SCOOTER_LOGO = By.CLASS_NAME, "Header_LogoScooter__3lsAR"
