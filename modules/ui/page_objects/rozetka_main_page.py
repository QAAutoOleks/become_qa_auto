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
        time.sleep(5)
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/div/div/rz-main-page/div/main/rz-main-page-content/rz-goods-sections/section[1]/rz-goods-section/ul/li[1]/rz-app-tile/div')))
        finally:
            pass
            #driver.quit()
        # sales_elements = self.driver.find_elements(
        #     By.CLASS_NAME, 'tile')
        time.sleep(3)
        print(len(elements))
