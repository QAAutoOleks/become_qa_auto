from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.rozetka_main_page import RozetkaMainPage
import pytest


# @pytest.mark.ui
# def test_check_incorrect_username_page_object():
#     sign_in_page = SignInPage()
#     sign_in_page.go_to()
#     sign_in_page.try_login('wrong.mail@mail.com', 'wrong_password')
#     assert sign_in_page.check_title('Sign in to GitHub · GitHub')
#     sign_in_page.close()

@pytest.mark.ui
def test_search_field():
    rozetka = RozetkaMainPage()
    rozetka.search_field()
    assert rozetka.driver.title == 'Ноутбуки - ROZETKA | Купити ноутбук в Києві: ціна, відгуки, продаж, вибір ноутбуків в Україні'
    assert rozetka.header == 'Ноутбуки'
    assert rozetka.first_good.find("Ноутбук") != -1
