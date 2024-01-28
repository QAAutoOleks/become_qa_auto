from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.rozetka_main_page import RozetkaMainPage
from modules.ui.page_objects.rozetka_laptops_page import RozetkaLaptopsPage
import pytest


@pytest.mark.ui_git
def test_check_incorrect_username_page_object():
    sign_in_page = SignInPage()
    sign_in_page.go_to()
    sign_in_page.try_login('wrong.mail@mail.com', 'wrong_password')
    assert sign_in_page.check_title('Sign in to GitHub · GitHub')
    sign_in_page.close()

@pytest.mark.ui_rozetka
def test_get_link_in_banner():
    rozetka = RozetkaMainPage()
    rozetka.banner_get_link()
    assert rozetka.link_in_banner == "https://rozetka.com.ua/ua/promo/rztk/"
    
    rozetka.driver.quit()

@pytest.mark.ui_rozetka
def test_close_banner():
    rozetka = RozetkaMainPage()
    assert rozetka.banner_close() != -1
    assert rozetka.banner_before_closed == True
    
    rozetka.driver.quit()

@pytest.mark.ui_rozetka
def test_search_field():
    rozetka = RozetkaMainPage()
    rozetka.search_field()
    assert rozetka.driver.title == 'Ноутбуки - ROZETKA | Купити ноутбук в Києві: ціна, відгуки, продаж, вибір ноутбуків в Україні'
    assert rozetka.header == 'Ноутбуки'
    assert rozetka.first_good.find("Ноутбук") != -1

    rozetka.driver.quit()

@pytest.mark.ui_rozetka
def test_menu_categories():
    rozetka = RozetkaMainPage()
    for link in rozetka.menu_categories():
        rozetka.go_to(link)
        assert rozetka.driver.title != rozetka.title_main_page
    
    rozetka.driver.quit()

@pytest.mark.ui_rozetka
def test_authorization_menu():
    rozetka = RozetkaMainPage()
    rozetka.authorization_menu()
    assert rozetka.popup_authorization.is_displayed()
    assert rozetka.popup_authorization_facebook.is_displayed()
    assert rozetka.popup_authorization_google.is_displayed()
    
    rozetka.remind_password.click()
    assert rozetka.popup_remind_password.is_displayed()

    rozetka.driver.quit()

@pytest.mark.ui_not_ready
def test_check_prices_sales_laptop():
    rozetka = RozetkaLaptopsPage()
    rozetka.check_sales_laptops_prices_displayed()

    counter_of_goods_tests = 0
    for element in rozetka.goods_list:
        if element.text.find('АКЦІЯ') != -1:
            index_search = element.text.find('₴')
            old_price = element.text[index_search-7:index_search]
            new_price = element.text[index_search+2:index_search+8]
            
            assert int(old_price.replace(" ", "")) > int(new_price.replace(" ", ""))
            
            counter_of_goods_tests += 1
            if counter_of_goods_tests == 5:
                break