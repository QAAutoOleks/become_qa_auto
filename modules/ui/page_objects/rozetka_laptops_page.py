from modules.ui.page_objects.rozetka_main_page import RozetkaMainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains 
import time


class RozetkaLaptopsPage(RozetkaMainPage):

    def __init__(self, link='https://rozetka.com.ua/ua/'):
        super().__init__(link='https://rozetka.com.ua/ua/notebooks/c80004/')
        self.action = ActionChains(self.driver)

    def finding_prices_on_page(self, quantity_of_tests):
        self.action.pause(2).perform()
        self.goods_list = self.driver.find_elements(
            By.XPATH, "//div[@class='goods-tile__content']")
        self.old_prices_list = []
        self.new_prices_list = []

        counter_of_goods_tests = 0
        for element in self.goods_list:
            self.driver.implicitly_wait(2)
            index_search = element.text.find('₴')
            old_price = element.text[index_search-7:index_search]

            old_price_int = RozetkaMainPage.convert_str_to_int(
                self, old_price)
            self.old_prices_list.append(old_price_int)

            new_price = element.text[index_search+1:index_search+9]
            new_price_int = RozetkaMainPage.convert_str_to_int(
                self, new_price)

            if new_price_int == 0:
                self.new_prices_list.append(old_price_int)
            else:
                self.new_prices_list.append(new_price_int)

            counter_of_goods_tests += 1
            if counter_of_goods_tests == quantity_of_tests:
                break

    def comparison_prices(self, quantity_of_tests):
        self.driver.implicitly_wait(3)
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
        sorting_button = Select(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
            By.XPATH, "/html/body/app-root/div/div/\
                rz-category/div/main/rz-catalog/div/\
                    rz-catalog-settings/div/rz-sort/select"))))
        sorting_button.select_by_visible_text("Від дорогих до дешевих")

    def get_titles_from_goods_tiles(self, quantity_goods):
        titles_list = []
        goods_list = self.driver.find_elements(
            By.XPATH, "//span[@class='goods-tile__title']")
        brands_name_inside_title = ""
        index = 0
        for element in goods_list:
            brands_name_inside_title = element.text
            titles_list.append(brands_name_inside_title)
            index += 1
            if index == quantity_goods:
                break

        return titles_list

    def select_checkbox_brand_ASUS(self):
        checkbox = self.driver.find_element(
            By.XPATH, "/html/body/app-root/div/div/rz-category/div/main/\
                rz-catalog/div/div/aside/rz-filter-stack/div[2]/div/\
                    rz-scrollbar/div/div[1]/div/div/rz-filter-section-autocomplete/\
                        ul[1]/li[1]/a")

        checkbox.click()

    def get_price_from_filters_field(self):
        self.range_filter_start = self.driver.find_element(
            By.XPATH, "/html/body/app-root/div/div/rz-category/div/\
                main/rz-catalog/div/div/aside/rz-filter-stack/div[3]/\
                    div/rz-scrollbar/div/div[1]/div/div/rz-filter-slider/\
                        form/fieldset/div/input[1]")
        self.range_filter_finish = self.driver.find_element(
            By.XPATH, "/html/body/app-root/div/div/rz-category/div/main/\
                rz-catalog/div/div/aside/rz-filter-stack/div[3]/div/\
                    rz-scrollbar/div/div[1]/div/div/rz-filter-slider/\
                        form/fieldset/div/input[2]")

    def changing_price_range_by_slider_filter(self):
        slider_start = self.driver.find_element(
            By.XPATH, "/html/body/app-root/div/div/rz-category/div/main/\
                rz-catalog/div/div/aside/rz-filter-stack/div[3]/div/\
                    rz-scrollbar/div/div[1]/div/div/rz-filter-slider/\
                        form/rz-range-slider/div/div/button[2]")
        slider_finish = self.driver.find_element(
            By.XPATH, "/html/body/app-root/div/div/rz-category/div/main/\
                rz-catalog/div/div/aside/rz-filter-stack/div[3]/div/\
                    rz-scrollbar/div/div[1]/div/div/rz-filter-slider/\
                        form/rz-range-slider/div/div/button[1]")

        self.action.move_to_element(slider_start).drag_and_drop(
            slider_start, slider_finish)
        self.action.pause(1)
        self.action.perform()

    def click_ok_button_in_fiters(self):
        ok_button = self.driver.find_element(
            By.XPATH, "/html/body/app-root/div/div/rz-category/div/main/\
                rz-catalog/div/div/aside/rz-filter-stack/div[3]/div/\
                    rz-scrollbar/div/div[1]/div/div/rz-filter-slider/\
                        form/fieldset/div/button")
        self.action.click(on_element = ok_button)                
        self.action.pause(1)
        self.action.perform()
