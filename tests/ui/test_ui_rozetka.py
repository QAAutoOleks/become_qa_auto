import pytest


@pytest.mark.ui_rozetka
def test_search_field_working(rozetka_main_page):
    rozetka_main_page.find_search_field_and_send_request()
    assert rozetka_main_page.driver.title == 'Ноутбуки - ROZETKA | Купити ноутбук в Києві: ціна, відгуки, продаж, вибір ноутбуків в Україні'
    assert rozetka_main_page.header_text == 'Ноутбуки'
    assert "Ноутбук" in rozetka_main_page.first_product_text
    assert "Ноутбук" in rozetka_main_page.second_product_text

    rozetka_main_page.driver.close()


@pytest.mark.ui_rozetka
def test_links_of_menu_categories_not_broken(rozetka_main_page):
    for link in rozetka_main_page.find_menu_categories_get_links():
        rozetka_main_page.go_to(link)
        assert rozetka_main_page.driver.title != rozetka_main_page.title_main_page

    rozetka_main_page.driver.close()


@pytest.mark.ui_rozetka
def test_authorization_menu_if_all_icons_displayed(rozetka_main_page):
    rozetka_main_page.find_authorization_menu()
    assert rozetka_main_page.popup_authorization.is_displayed()
    assert rozetka_main_page.popup_authorization_facebook.is_displayed()
    assert rozetka_main_page.popup_authorization_google.is_displayed()

    rozetka_main_page.remind_password.click()
    assert rozetka_main_page.popup_remind_password.is_displayed()

    rozetka_main_page.driver.close()


@pytest.mark.ui_rozetka
def test_icons_of_social_networks_on_main_page_is_displayed(rozetka_main_page):
    for icon in rozetka_main_page.find_social_networks_icons():
        assert icon.is_displayed

    rozetka_main_page.driver.close()


# quantity of goods required to be tested is flexible
# quantity_of_tests = 3
@pytest.mark.ui_rozetka
def test_check_prices_sales_laptop(rozetka_laptops_page):
    quantity_of_tests = 3
    rozetka_laptops_page.comparison_prices(quantity_of_tests)
    rozetka_laptops_page.finding_prices_on_page(quantity_of_tests)

    index = 0
    for price in rozetka_laptops_page.new_prices_list:
        assert int(price) < int(rozetka_laptops_page.old_prices_list[index])
        assert price == rozetka_laptops_page.prices_on_goods_pages_list[index]
        index += 1

    rozetka_laptops_page.driver.close()


# quantity of goods required to be tested is flexible
# quantity_of_tests = 5
@pytest.mark.ui_rozetka
def test_select_sorting_by_price(rozetka_laptops_page):
    quantity_of_tests = 5

    rozetka_laptops_page.select_sorting("Від дорогих до дешевих")

    rozetka_laptops_page.finding_prices_on_page(quantity_of_tests)
    price_down_list = rozetka_laptops_page.new_prices_list

    if len(price_down_list) > 1:
        for i in range(1, quantity_of_tests):
            assert price_down_list[i] < price_down_list[i - 1]

    rozetka_laptops_page.select_sorting("Від дешевих до дорогих")

    rozetka_laptops_page.finding_prices_on_page(quantity_of_tests)
    price_up_list = rozetka_laptops_page.new_prices_list

    if len(price_up_list) > 1:
        for i in range(1, quantity_of_tests):
            assert (price_up_list[i] >= price_up_list[i - 1] and
                    price_up_list[i] < price_down_list[i])

    rozetka_laptops_page.driver.close()


# Method .get_titles_from_goods_tiles() is checking goods titles
# and check if names of goods include brand which selected in filters - ASUS.
# Instead of ASUS it is possible to specify another brand:
# Acer, Apple, Dell, Gigabyte, HP etc.
#
# Necessary quantity of goods titles is entering in parentheses
# depending on the needs
@pytest.mark.ui_rozetka
def test_checkbox_filter_by_brand(rozetka_laptops_page):
    brand_name = 'ASUS'
    rozetka_laptops_page.select_checkbox_brand(brand_name)

    for brand_from_title in rozetka_laptops_page.get_titles_from_goods_tiles(5):
        assert brand_name in brand_from_title

    rozetka_laptops_page.driver.close()


# quantity of goods required to be tested is flexible
# finding_prices_on_page(3)
@pytest.mark.ui_rozetka
def test_changing_price_range_by_fiters(rozetka_laptops_page):
    rozetka_laptops_page.get_price_from_filters_field()
    rozetka_laptops_page.changing_price_range_by_slider_filter()
    value_from_field = rozetka_laptops_page.range_filter_finish.get_attribute(
        'value')

    assert rozetka_laptops_page.range_filter_start.get_attribute(
        'value') == value_from_field

    rozetka_laptops_page.click_ok_button_in_fiters()

    rozetka_laptops_page.finding_prices_on_page(3)
    element = rozetka_laptops_page.range_filter_finish
    assert rozetka_laptops_page.new_prices_list[0] <= int(value_from_field)

    rozetka_laptops_page.driver.close()


@pytest.mark.ui_rozetka
def test_price_in_goods_page_and_at_cart_popup(rozetka_goods_page):
    price_on_page = rozetka_goods_page.find_price_goods_page()
    rozetka_goods_page.find_and_click_to_buy_button()
    price_in_cart = rozetka_goods_page.find_price_in_popup_window_cart()
    assert price_on_page == price_in_cart

    rozetka_goods_page.driver.close()


@pytest.mark.ui_rozetka
def test_change_quantity_of_goods_in_cart(rozetka_goods_page):
    rozetka_goods_page.find_and_click_to_buy_button()
    rozetka_goods_page.change_quantity_in_cart()
    price_in_cart = rozetka_goods_page.find_price_in_popup_window_cart()
    rozetka_goods_page.plus_button_in_cart_window.click()
    changed_price = rozetka_goods_page.find_price_in_popup_window_cart()

    assert changed_price == 2 * price_in_cart

    rozetka_goods_page.minus_button_in_cart_window.click()
    changed_price = rozetka_goods_page.find_price_in_popup_window_cart()
    assert changed_price == price_in_cart

    rozetka_goods_page.driver.close()


@pytest.mark.ui_rozetka
def test_adding_extra_services_guarantee(rozetka_goods_page):
    price_on_page = rozetka_goods_page.find_price_goods_page()
    rozetka_goods_page.add_extra_services()
    rozetka_goods_page.find_and_click_to_buy_button()
    changed_price = rozetka_goods_page.find_price_in_popup_window_cart()
    price_of_extra_service = rozetka_goods_page.find_price_of_extra_service()

    assert price_of_extra_service + price_on_page == changed_price

    rozetka_goods_page.driver.close()
