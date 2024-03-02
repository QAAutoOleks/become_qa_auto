from modules.ui.page_objects.rozetka_main_page import RozetkaMainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class RozetkaGoodsPage(RozetkaMainPage):

    def __init__(self, link='https://rozetka.com.ua/ua/'):
        super().__init__(link='https://rozetka.com.ua/ua/lenovo-82rk011nra/p400966992/')

    def find_price_goods_page(self):
        self.action.pause(2).perform()
        price = self.driver.find_element(
            By.CSS_SELECTOR, '.product-price__big-color-red')

        old_price_int = RozetkaGoodsPage.convert_str_to_int(
            self, price.text)

        return int(old_price_int)

    def find_price_in_popup_window_cart(self):
        self.action.pause(2).perform()
        price_in_cart = self.driver.find_element(
            By.CSS_SELECTOR, '.cart-product__price--red')

        price_in_cart_int = RozetkaGoodsPage.convert_str_to_int(
            self, price_in_cart.text)

        return price_in_cart_int

    def find_and_click_to_buy_button(self):
        button_to_buy = self.driver.find_element(
            By.CSS_SELECTOR, '.product-button__buy')

        self.action.pause(1).click(on_element=button_to_buy).pause(2).perform() #

    def change_quantity_in_cart(self):
        self.plus_button_in_cart_window = self.driver.find_element(
            By.XPATH, "/html/body/app-root/rz-single-modal-window/\
                div[3]/div[2]/rz-shopping-cart/div/rz-purchases/\
                    ul/li/rz-cart-product/div/div[2]/\
                        rz-cart-counter/div/button[2]")
        self.minus_button_in_cart_window = self.driver.find_element(
            By.XPATH, "/html/body/app-root/rz-single-modal-window/\
                div[3]/div[2]/rz-shopping-cart/div/rz-purchases/\
                    ul/li/rz-cart-product/div/div[2]/\
                        rz-cart-counter/div/button[1]")

    def add_extra_services(self):
        checkbox_guarantee_services = self.driver.find_element(
            By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/\
            rz-product-main-info/rz-product-services/div/\
                rz-additional-services/div/rz-service-group[1]/\
                    div/div/label'
        )
        checkbox_guarantee_services.click()

    def find_price_of_extra_service_guarantee(self):
        price_of_extra_service = self.driver.find_element(
            By.XPATH, "/html/body/app-root/rz-single-modal-window/\
                div[3]/div[2]/rz-shopping-cart/div/rz-purchases/\
                    ul/li/rz-cart-product/div/rz-cart-additional-services/\
                        div/rz-additional-services/div/rz-service-group[1]/\
                            div/ul/li[1]/rz-service-product/div/div/label/\
                                div/div[2]/div")
        price_int = RozetkaGoodsPage.convert_str_to_int(
            self, price_of_extra_service.text)

        return price_int
