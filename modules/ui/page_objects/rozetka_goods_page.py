from modules.ui.page_objects.rozetka_main_page import RozetkaMainPage
from selenium.webdriver.common.by import By


class RozetkaGoodsPage(RozetkaMainPage):

    def __init__(self, link='https://rozetka.com.ua/ua/'):
        super().__init__(link='https://rozetka.com.ua/ua/lenovo-82rk011nra/p400966992/')

    def find_price_goods_page(self):
        self.action.pause(2).perform()
        price = self.driver.find_element(
            By.CSS_SELECTOR, '.product-price__big-color-red'
        )

        old_price_int = RozetkaGoodsPage.convert_str_to_int(
            self, price.text)

        return int(old_price_int)

    def find_price_in_popup_window_cart(self):
        self.action.pause(2).perform()
        price_in_cart = self.driver.find_element(
            By.CSS_SELECTOR, '.cart-receipt__sum-price'
        )

        price_in_cart_int = RozetkaGoodsPage.convert_str_to_int(
            self, price_in_cart.text)

        return price_in_cart_int

    def find_and_click_to_buy_button(self):
        button_to_buy = self.driver.find_element(
            By.CSS_SELECTOR, '.product-button__buy'
        )

        self.action.pause(1).click(on_element=button_to_buy).pause(2).perform()

    def change_quantity_in_cart(self):
        self.plus_button_in_cart_window = self.driver.find_element(
            By.CSS_SELECTOR, '[data-testid="cart-counter-increment-button"]'
        )
        self.minus_button_in_cart_window = self.driver.find_element(
            By.CSS_SELECTOR, '[data-testid="cart-counter-decrement-button"]'
        )
    # Method adds extra services to cart with product
    # for next verification changes total amount of purchase
    # displayed in cart
    def add_extra_services(self):
        checkbox_extra_services = self.driver.find_element(
            By.CSS_SELECTOR, '[for="serviceGroup2614_0"]'
        )
        checkbox_extra_services.click()

    def find_price_of_extra_service(self):
        extra_service_label = self.driver.find_element(
            By.CSS_SELECTOR, '.service-product__label'
        )
        price_of_extra_service = extra_service_label.find_element(
            By.CSS_SELECTOR, '.service-product__price'
        )
        price_int = RozetkaGoodsPage.convert_str_to_int(
            self, price_of_extra_service.text)

        return price_int
