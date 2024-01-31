from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains 
import time

class RozetkaGoodsPage(BasePage):

    def __init__(self):
        super().__init__()
        RozetkaGoodsPage.go_to(self)
        self.action = ActionChains(self.driver)

    def go_to(self, link='https://rozetka.com.ua/ua/lenovo-82rk011nra/p400966992/'):
        self.driver.get(link)

    def find_price(self):
        old_price = self.driver.find_element(
            By.XPATH, '//*[@id="#scrollArea"]/div[1]/\
            div[2]/rz-product-main-info/div[1]/div[1]/\
                div[1]/p[1]')
        print(old_price.text)