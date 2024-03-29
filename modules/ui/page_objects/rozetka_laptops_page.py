from modules.ui.page_objects.rozetka_main_page import RozetkaMainPage
from modules.ui.page_objects.rozetka_goods_page import RozetkaGoodsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class RozetkaLaptopsPage(RozetkaMainPage):

    def __init__(self, link='https://rozetka.com.ua/ua/'):
        super().__init__(link='https://rozetka.com.ua/ua/notebooks/c80004/')

    # Method finds prices for any number of goods in catalogs. 
    # Required quantity of goods ('quantity_of_tests') 
    # is set depending on the needs.
    # Method is used in tests of changing prices after 
    # filters application, promotional prices.
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
            old_price = element.text[index_search - 7:index_search]

            old_price_int = RozetkaMainPage.convert_str_to_int(
                self, old_price)
            self.old_prices_list.append(old_price_int)

            new_price = element.text[index_search + 1:index_search + 9]
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
            price_on_goods_page = RozetkaGoodsPage.find_price_goods_page(self)
            self.prices_on_goods_pages_list.append(price_on_goods_page)

            counter_of_goods_tests += 1
            if counter_of_goods_tests == quantity_of_tests:
                break

    def select_sorting(self, sort):
        sorting_button = Select(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, ".select-css"))))
        sorting_button.select_by_visible_text(sort)

    def get_titles_from_goods_tiles(self, quantity_goods):
        titles_list = []
        self.action.pause(2).perform()
        goods_list = self.driver.find_elements(
            By.XPATH, "//span[@class='goods-tile__title']")
        index = 0
        for element in goods_list:
            brands_name_inside_title = element.text
            titles_list.append(brands_name_inside_title)
            index += 1
            if index == quantity_goods:
                break

        return titles_list

    def select_checkbox_brand(self, brand):
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, f'[data-id={brand}]')))

        checkbox.click()

    def get_price_from_filters_field(self):
        self.range_filter_start = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '[formcontrolname="min"]')))
        self.range_filter_finish = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '[formcontrolname="max"]')))

    def changing_price_range_by_slider_filter(self):
        slider_start = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.rz-slider__range-button_type_right')))
        slider_finish = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.rz-slider__range-button_type_left')))

        self.action.move_to_element(slider_start).drag_and_drop(
            slider_start, slider_finish)
        self.action.pause(2)
        self.action.perform()

    def click_ok_button_in_fiters(self):
        ok_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.slider-filter__button')))
        self.action.click(on_element=ok_button)
        self.action.pause(1)
        self.action.perform()

