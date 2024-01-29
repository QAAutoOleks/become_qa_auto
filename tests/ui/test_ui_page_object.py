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

@pytest.mark.rozetka
def test_check_prices_sales_laptop():
    rozetka = RozetkaLaptopsPage()
    rozetka.comparison_prices(3)
    rozetka.finding_prices_on_page(3)

    index = 0
    for price in rozetka.new_prices_list:
        assert int(price) < int(rozetka.old_prices_list[index])
        assert price == rozetka.prices_on_goods_pages_list[index]
        index += 1

    rozetka.driver.quit()

@pytest.mark.ui_not_ready
def test_select_sorting():
    quantity_of_tests = 3
    rozetka = RozetkaLaptopsPage()
    rozetka.finding_prices_on_page(quantity_of_tests)
    price_before_sorting = rozetka.new_prices_list

    rozetka.select_sorting()

    rozetka.finding_prices_on_page(quantity_of_tests)
    price_after_sorting = rozetka.new_prices_list

    assert price_before_sorting != price_after_sorting
    is_sort_low_to_high = True
    index = 0
    if len(price_after_sorting) > 1:
        for i in range(1, quantity_of_tests):
            assert price_after_sorting[i] < price_after_sorting[i-1]
    
    rozetka.driver.close()

# @pytest.mark.ui
# def 