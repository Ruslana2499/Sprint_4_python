from pages.home_page import HomePageObject


def test_drop_down_list(open_home):
    driver = open_home
    home = HomePageObject(driver)
    home.click_accept_cookies_button()
    ids = home.get_drop_down_list_ids()
    for id in ids:
        home.click_drop_down_list_item(id)
        assert id == home.get_visible_drop_down_list_text_block_id()
def test_drop_down_list_first_item(prepare_home_page):
    home = prepare_home_page
    home.click_drop_down_list_item('0')
    assert "0" == home.get_visible_drop_down_list_text_block_id()

def test_drop_down_list_second_item(prepare_home_page):
    home = prepare_home_page
    home.click_drop_down_list_item('1')
    assert "1" == home.get_visible_drop_down_list_text_block_id()

def test_drop_down_list_third_item(prepare_home_page):
    home = prepare_home_page
    home.click_drop_down_list_item('2')
    assert "2" == home.get_visible_drop_down_list_text_block_id()

def test_drop_down_list_fourth_item(prepare_home_page):
    home = prepare_home_page
    home.click_drop_down_list_item('3')
    assert "3" == home.get_visible_drop_down_list_text_block_id()

def test_drop_down_list_fifth_item(prepare_home_page):
    home = prepare_home_page
    home.click_drop_down_list_item('4')
    assert "4" == home.get_visible_drop_down_list_text_block_id()

def test_drop_down_list_sixth_item(prepare_home_page):
    home = prepare_home_page
    home.click_drop_down_list_item('5')
    assert "5" == home.get_visible_drop_down_list_text_block_id()

def test_drop_down_list_seventh_item(prepare_home_page):
    home = prepare_home_page
    home.click_drop_down_list_item('6')
    assert "6" == home.get_visible_drop_down_list_text_block_id()

def test_drop_down_list_seventh_item(prepare_home_page):
    home = prepare_home_page
    home.click_drop_down_list_item('7')
    assert "7" == home.get_visible_drop_down_list_text_block_id()