from pages.home_page import HomePageObject


def test_drop_down_list(open_home):
    driver = open_home
    home = HomePageObject(driver)
    home.click_accept_cookies_button()
    ids = home.get_drop_down_list_ids()
    for id in ids:
        home.click_drop_down_list_item(id)
        assert id == home.get_visible_drop_down_list_text_block_id()
    # закрыть браузер
    driver.quit()
