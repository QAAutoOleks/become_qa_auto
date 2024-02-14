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

    def find_search_field_and_send_request(self):
        search_feald = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
            By.CSS_SELECTOR, "input[placeholder='Я шукаю...']")))
        search_feald.send_keys('laptop')
        button = self.driver.find_element(
            By.XPATH, "//button[contains(text(),'Знайти')]")
        button.click()

        header = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/\
                div/rz-category/div/main/div[1]/div/h1")))
        self.header_text = header.text

        first_good = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
            By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/div[1]\
                /rz-category[1]/div[1]/main[1]/rz-catalog[1]/div[1]\
                    /div[1]/section[1]/rz-grid[1]/ul[1]/li[1]\
                        /rz-catalog-tile[1]/app-goods-tile-default[1]\
                            /div[1]/div[2]/div[1]/rz-button-product-page[2]/a[1]"
        )))
        self.first_goods = str(first_good.text)

    def find_menu_categories_get_links(self):
        self.title_main_page = self.driver.title
        links_list = []
        menu_list = self.driver.find_elements(
            By.XPATH, "//a[@class='menu-categories__link']")

        for element in menu_list:
            link = element.get_attribute('href')
            links_list.append(link)

        return links_list

    def find_authorization_menu(self):
        authorization_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
            By.XPATH, "/html/body/app-root/div/div/rz-header/\
                rz-main-header/header/div/div/ul/li[3]/rz-user/button")))
        authorization_button.click()

        self.popup_authorization = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
            By.XPATH, "//div[@class='modal__content']")))
        self.popup_authorization_facebook = self.driver.find_element(
            By.XPATH, "/html/body/app-root/rz-single-modal-window/\
                div[3]/div[2]/rz-user-identification/rz-auth/div/\
                    div/div/rz-social-auth/button[1]")
        self.popup_authorization_google = self.driver.find_element(
            By.XPATH, "/html/body/app-root/rz-single-modal-window/\
                div[3]/div[2]/rz-user-identification/rz-auth/div/\
                    div/div/rz-social-auth/button[1]")
        self.remind_password = self.driver.find_element(
            By.XPATH, "/html/body/app-root/rz-single-modal-window/\
                div[3]/div[2]/rz-user-identification/rz-auth/div/\
                    form/fieldset/div[3]/a")
        self.popup_remind_password = self.driver.find_element(
            By.XPATH, "/html/body/app-root/rz-single-modal-window/\
                div[3]/div[2]")

    def find_social_networks_icons(self):
        time.sleep(1)
        all_socials_networks_icons = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
            By.CLASS_NAME, "socials__list")))
        each_icon_list = all_socials_networks_icons.find_elements(
            By.TAG_NAME, "li")

        return each_icon_list
