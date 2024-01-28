from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.rozetka_main_page import RozetkaMainPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    sign_in_page = SignInPage()
    sign_in_page.go_to()
    sign_in_page.try_login('wrong.mail@mail.com', 'wrong_password')
    assert sign_in_page.check_title('Sign in to GitHub · GitHub')
    sign_in_page.close()

@pytest.mark.ui
def test_get_link_in_banner():
    rozetka = RozetkaMainPage()
    rozetka.banner_get_link()
    assert rozetka.link_in_banner == "https://rozetka.com.ua/ua/promo/rztk/"

@pytest.mark.ui
def test_close_banner():
    rozetka = RozetkaMainPage()
    assert rozetka.banner_close() != -1
    assert rozetka.banner_before_closed == True

@pytest.mark.ui
def test_search_field():
    rozetka = RozetkaMainPage()
    rozetka.search_field()
    assert rozetka.driver.title == 'Ноутбуки - ROZETKA | Купити ноутбук в Києві: ціна, відгуки, продаж, вибір ноутбуків в Україні'
    assert rozetka.header == 'Ноутбуки'
    assert rozetka.first_good.find("Ноутбук") != -1

@pytest.mark.ui
def test_menu_categories():
    rozetka = RozetkaMainPage()
    for link in rozetka.menu_categories():
        rozetka.go_to(link)
        assert rozetka.driver.title != rozetka.title_main_page

@pytest.mark.ui
def test_authorization_menu():
    rozetka = RozetkaMainPage()
    rozetka.authorization_menu()
    assert rozetka.popup_authorization.is_displayed()
    assert rozetka.popup_authorization_facebook.is_displayed()
    assert rozetka.popup_authorization_google.is_displayed()
    
    rozetka.remind_password.click()
    assert rozetka.popup_remind_password.is_displayed()
