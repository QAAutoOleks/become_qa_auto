from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class RozetkaMainPage(BasePage):

    def __init__(self):
        super().__init__()

    def go_to(self, link='https://rozetka.com.ua/ua/'):
        self.driver.get(link)

    def sales_elements(self):
        time.sleep(2)        
        sales = self.driver.find_elements(
            By.CSS_SELECTOR, '.tile')
        for i in sales:
            print("element:", i)
