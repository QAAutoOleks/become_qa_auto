from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class RozetkaLaptopsPage(BasePage):

    def __init__(self):
        super().__init__()
        RozetkaLaptopsPage.go_to(self)

    def go_to(self, link='https://rozetka.com.ua/ua/notebooks/c80004/'):
        self.driver.get(link)

    def comparison_prices(self, quantity_of_tests):
        self.driver.implicitly_wait(1)
        self.goods_list = self.driver.find_elements(
            By.XPATH, "//div[@class='goods-tile__content']")
        self.old_prices_list = []
        self.new_prices_list = []
        self.links_on_goods = []
        self.prices_on_goods_pages_list = []

        counter_of_goods_tests = 0
        for element in self.goods_list:
            if element.text.find('АКЦІЯ') != -1:
                index_search = element.text.find('₴')
                old_price = element.text[index_search-6:index_search]
                self.old_prices_list.append(old_price.replace(" ", ""))
                new_price = element.text[index_search+2:index_search+8]
                self.new_prices_list.append(new_price.replace(" ", ""))

                href = element.find_element(By.TAG_NAME, 'a')
                link = href.get_attribute('href')
                self.links_on_goods.append(link)

                counter_of_goods_tests += 1
                if counter_of_goods_tests == quantity_of_tests:
                    break

        for link in self.links_on_goods:
            RozetkaLaptopsPage.go_to(self, link)
            price_on_goods_page = self.driver.find_element(
                By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/\
                    rz-product-main-info/div[1]/div[1]/div[1]/p[2]')
            price = price_on_goods_page.text[:6]
            self.prices_on_goods_pages_list.append(price.replace(" ", ""))
