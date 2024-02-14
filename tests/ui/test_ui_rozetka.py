import pytest
from modules.ui.page_objects.rozetka_main_page import RozetkaMainPage
from modules.ui.page_objects.rozetka_laptops_page import RozetkaLaptopsPage
from modules.ui.page_objects.rozetka_goods_page import RozetkaGoodsPage


@pytest.mark.ui_not_ready
def test_search_field_working():
    rozetka = RozetkaMainPage()
    rozetka.find_search_field_and_send_request()
    assert rozetka.driver.title == 'Ноутбуки - ROZETKA | Купити ноутбук в Києві: ціна, відгуки, продаж, вибір ноутбуків в Україні'
    assert rozetka.header_text == 'Ноутбуки'
    assert rozetka.first_good.find("Ноутбук") != -1

    rozetka.driver.close()


@pytest.mark.ui_not_ready
def test_links_of_menu_categories_not_broken():
    rozetka = RozetkaMainPage()
    for link in rozetka.find_menu_categories_get_links():
        rozetka.go_to(link)
        assert rozetka.driver.title != rozetka.title_main_page

    rozetka.driver.close()


@pytest.mark.ui_not_ready
def test_authorization_menu_if_all_icons_displayed():
    rozetka = RozetkaMainPage()
    rozetka.find_authorization_menu()
    assert rozetka.popup_authorization.is_displayed()
    assert rozetka.popup_authorization_facebook.is_displayed()
    assert rozetka.popup_authorization_google.is_displayed()

    rozetka.remind_password.click()
    assert rozetka.popup_remind_password.is_displayed()

    rozetka.driver.close()

@pytest.mark.ui_not_ready
def test_icons_of_social_networks_on_main_page_is_displayed():
    rozetka = RozetkaMainPage()

    for icon in rozetka.find_social_networks_icons():
        assert icon.is_displayed
    
    rozetka.driver.close()

@pytest.mark.ui_not_ready
def test_check_prices_sales_laptop():
    rozetka = RozetkaLaptopsPage()
    rozetka.comparison_prices(3)
    rozetka.finding_prices_on_page(3)

    index = 0
    for price in rozetka.new_prices_list:
        assert int(price) < int(rozetka.old_prices_list[index])
        assert price == rozetka.prices_on_goods_pages_list[index]
        index += 1

    rozetka.driver.close()


@pytest.mark.ui_not_ready
def test_select_sorting_from_high_to_low_price():
    quantity_of_tests = 3
    rozetka = RozetkaLaptopsPage()
    rozetka.finding_prices_on_page(quantity_of_tests)
    price_before_sorting = rozetka.new_prices_list

    rozetka.select_sorting()

    rozetka.finding_prices_on_page(quantity_of_tests)
    price_after_sorting = rozetka.new_prices_list

    assert price_before_sorting != price_after_sorting

    index = 0
    if len(price_after_sorting) > 1:
        for i in range(1, quantity_of_tests):
            assert price_after_sorting[i] < price_after_sorting[i-1]

    rozetka.driver.close()


@pytest.mark.ui_rozetka
def test_checkbox_filter_by_brand():
    rozetka = RozetkaLaptopsPage()
    rozetka.select_checkbox_brand_ASUS()
    for brand in rozetka.get_titles_from_goods_tiles(5):
        assert brand.find("ASUS") != -1

    rozetka.driver.close()


@pytest.mark.ui_rozetka
def test_changing_price_range_by_fiters():
    rozetka = RozetkaLaptopsPage()
    rozetka.get_price_from_filters_field()
    rozetka.changing_price_range_by_slider_filter()
    value_from_field = rozetka.range_filter_finish.get_attribute('value')

    assert rozetka.range_filter_start.get_attribute(
        'value') == value_from_field        

    rozetka.click_ok_button_in_fiters()

    rozetka.finding_prices_on_page(1)
    element = rozetka.range_filter_finish
    assert rozetka.new_prices_list[0] <= int(value_from_field)

    rozetka.driver.close()

@pytest.mark.ui_rozetka
def test_price_in_goods_page_and_at_cart_popup():
    rozetka = RozetkaGoodsPage()
    price_on_page = rozetka.find_price_goods_page()
    rozetka.find_and_click_to_buy_button()
    price_in_cart = rozetka.find_price_in_popup_window_cart()
    assert price_on_page == price_in_cart

    rozetka.driver.close()

@pytest.mark.ui_rozetka
def test_change_quantity_of_goods_in_cart():
    rozetka = RozetkaGoodsPage()
    rozetka.find_and_click_to_buy_button()
    rozetka.change_quantity_in_cart()
    price_in_cart = rozetka.find_price_in_popup_window_cart()
    rozetka.plus_button_in_cart_window.click()
    changed_price = rozetka.find_price_in_popup_window_cart()

    assert changed_price == 2 * price_in_cart

    rozetka.minus_button_in_cart_window.click()
    changed_price = rozetka.find_price_in_popup_window_cart()
    assert changed_price == price_in_cart

    rozetka.driver.close()

@pytest.mark.ui_rozetka
def test_adding_extra_services_guarantee():
    rozetka = RozetkaGoodsPage()
    price_on_page = rozetka.find_price_goods_page()
    rozetka.add_extra_services()
    rozetka.find_and_click_to_buy_button()
    changed_price = rozetka.find_price_in_popup_window_cart()
    price_of_extra_service = rozetka.find_price_of_extra_service_guarantee()
    
    assert price_of_extra_service + price_on_page == changed_price

    rozetka.driver.close()

