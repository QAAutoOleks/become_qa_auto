from modules.ui.page_objects.rozetka_main_page import RozetkaMainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class RozetkaGoodsPage(RozetkaMainPage):

    def __init__(self, link='https://rozetka.com.ua/ua/'):
        super().__init__(link='https://rozetka.com.ua/ua/lenovo-82rk011nra/p400966992/')
        self.action = ActionChains(self.driver)

    def find_price_goods_page(self):
        self.action.pause(1).perform()
        old_price = self.driver.find_element(
            By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/\
            rz-product-main-info/div[1]/div[1]/div[1]/p[2]')

        old_price_int = RozetkaGoodsPage.convert_str_to_int(
            self, old_price.text)

        return int(old_price_int)

    def find_price_in_popup_window_cart(self):
        self.action.pause(1).perform()
        price_in_cart = self.driver.find_element(
            By.XPATH, "/html/body/app-root/rz-single-modal-window/\
                div[3]/div[2]/rz-shopping-cart/div/div[1]/\
                    div/div/div/span")

        price_in_cart_int = RozetkaGoodsPage.convert_str_to_int(
            self, price_in_cart.text)

        return price_in_cart_int

    def find_and_click_to_buy_button(self):
        button_to_buy = self.driver.find_element(
            By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/\
            rz-product-main-info/div[1]/div[1]/div[3]/\
                rz-product-buy-btn/app-buy-button/button')

        self.action.pause(1).click(on_element=button_to_buy).pause(1).perform()

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
        checkbox_garanty_services = self.driver.find_element(
            By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/\
            rz-product-main-info/rz-product-services/div/\
                rz-additional-services/div/rz-service-group[1]/\
                    div/div/label'
        )
        checkbox_garanty_services.click()

    def find_price_of_extra_service_garanty(self):
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
