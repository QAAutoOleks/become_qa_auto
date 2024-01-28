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

    def check_sales_laptops_prices_displayed(self):
        self.goods_list = self.driver.find_elements(By.XPATH, "//div[@class='goods-tile__content']")
