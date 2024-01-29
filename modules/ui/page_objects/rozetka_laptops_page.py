from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


class RozetkaLaptopsPage(BasePage):

    def __init__(self):
        super().__init__()
        RozetkaLaptopsPage.go_to(self)

    def go_to(self, link='https://rozetka.com.ua/ua/notebooks/c80004/'):
        self.driver.get(link)

    def finding_prices_on_page(self, quantity_of_tests):
        self.driver.implicitly_wait(2)
        self.goods_list = self.driver.find_elements(
            By.XPATH, "//div[@class='goods-tile__content']")
        self.old_prices_list = []
        self.new_prices_list = []

        counter_of_goods_tests = 0
        for element in self.goods_list:
            index_search = element.text.find('₴')
            old_price = element.text[index_search-7:index_search]
            old_price_digital = ""

            for p in old_price:
                if p.isnumeric():
                    old_price_digital += p
            self.old_prices_list.append(int(old_price_digital))

            new_price = element.text[index_search+1:index_search+9]
            new_price_digital = ""

            for p in new_price:
                if p.isnumeric():
                    new_price_digital += p
            if new_price_digital == "":
                self.new_prices_list.append(int(old_price_digital))
            else:
                self.new_prices_list.append(int(new_price_digital))

            counter_of_goods_tests += 1
            if counter_of_goods_tests == quantity_of_tests:
                break

    def comparison_prices(self, quantity_of_tests):
        self.driver.implicitly_wait(1)
        RozetkaLaptopsPage.finding_prices_on_page(self, quantity_of_tests)

        self.prices_on_goods_pages_list = []
        self.links_on_goods = []
        for element in self.goods_list:
            if element.text.find('АКЦІЯ') != -1:
                href = element.find_element(By.TAG_NAME, 'a')
                link = href.get_attribute('href')
                self.links_on_goods.append(link)

        counter_of_goods_tests = 0
        for link in self.links_on_goods:
            RozetkaLaptopsPage.go_to(self, link)
            price_on_goods_page = self.driver.find_element(
                By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/\
                    rz-product-main-info/div[1]/div[1]/div[1]/p[2]')
            price = price_on_goods_page.text[:6]
            price_after_sorting = price_on_goods_page.text[:]
            self.prices_on_goods_pages_list.append(price.replace(" ", ""))

            counter_of_goods_tests += 1
            if counter_of_goods_tests == quantity_of_tests:
                break

    def select_sorting(self):
        sorting_button = Select(self.driver.find_element(
            By.XPATH, "/html/body/app-root/div/div/\
                rz-category/div/main/rz-catalog/div/\
                    rz-catalog-settings/div/rz-sort/select"))
        sorting_button.select_by_visible_text("Від дорогих до дешевих")
        time.sleep(3)
