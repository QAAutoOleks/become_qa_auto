from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class RozetkaMainPage(BasePage):

    def __init__(self):
        super().__init__()
        RozetkaMainPage.go_to(self)

    def go_to(self, link='https://rozetka.com.ua/ua/'):
        self.driver.get(link)


    def search_field(self):
        time.sleep(1)
        search_feald = self.driver.find_element(
            By.CSS_SELECTOR, "input[placeholder='Я шукаю...']")
        search_feald.send_keys('laptop')
        time.sleep(2)
        button = self.driver.find_element(
            By.XPATH, "//button[contains(text(),'Знайти')]")
        button.click()
        time.sleep(2)
        self.header = self.driver.find_element(
            By.XPATH, "//h1[contains(text(),'Ноутбуки')]").text
        first_good = self.driver.find_element(
            By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/div[1]\
                /rz-category[1]/div[1]/main[1]/rz-catalog[1]/div[1]\
                    /div[1]/section[1]/rz-grid[1]/ul[1]/li[1]\
                        /rz-catalog-tile[1]/app-goods-tile-default[1]\
                            /div[1]/div[2]/div[1]/rz-button-product-page[2]/a[1]"
        ).text
        self.first_good = str(first_good)
