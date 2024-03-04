from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class RozetkaMainPage(BasePage):

    def __init__(self, link='https://rozetka.com.ua/ua/'):
        super().__init__()
        RozetkaMainPage.go_to(self, link)

        # For tests which require input actions to the web browser is
        # created object of ActionChains class.
        # 
        # ActionChains objects are used in tests which need to wait 
        # certain time between actions for working correctly.
        # Beyond that ActionChains objects are used for manipulations 
        # with the mouse during performing tests (moving slider in filters,
        # click on buy button on the goods page etc.).
        self.action = ActionChains(self.driver)

    def go_to(self, link):
        self.driver.get(link)

    # Method is applied for conversion String data to Integer data
    # from Web elements in price comparison tests such as:
    # increase of purchase amount after adding guarantee service,
    # selection sorting from high to low price,
    # price comparison on goods card in the general catalog 
    # and on the product page, etc.
    def convert_str_to_int(self, str_input):
        str_digital = ""
        for symbol in str_input:
            if symbol.isnumeric():
                str_digital += symbol

        if len(str_digital) > 0:
            return int(str_digital)
        else:
            return 0

    # Method for checking functionality of search field.
    # Enter query in the search field. After reloading 
    # the page, checking the page header and 
    # goods name in catalog.
    def find_search_field_and_send_request(self):
        search_feald = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, "input[placeholder='Я шукаю...']")))
        search_feald.send_keys('laptop')
        button = self.driver.find_element(
            By.CSS_SELECTOR, ".search-form__submit")
        button.click()

        header = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.catalog-heading')))
        self.header_text = header.text

        goods_titles = self.driver.find_elements(
            By.CSS_SELECTOR, '.goods-tile__title'
        )
        self.first_product_text = goods_titles[0].text
        self.second_product_text = goods_titles[1].text

    # Checking links of menu categories isn't broken
    def find_menu_categories_get_links(self):
        self.title_main_page = self.driver.title
        links_list = []
        menu_list = self.driver.find_elements(
            By.XPATH, "//a[@class='menu-categories__link']")

        for element in menu_list:
            link = element.get_attribute('href')
            links_list.append(link)

        return links_list

    # Checking authorization button and icons in 
    # authorization menu are displayed (Facebook, 
    # Google, Remind password etc.).
    def find_authorization_menu(self):
        authorization_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH, "//rz-user[@_ngcontent-rz-client-c271359985]/button")))
        self.action.pause(2).click(
            on_element=authorization_button).pause(2).perform()

        self.popup_authorization = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH, "//div[@class='modal__content']")))
        self.popup_authorization_facebook = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Facebook')]")
        self.popup_authorization_google = self.driver.find_element(
            By.XPATH, '(//button[normalize-space()="Google"])[1]')
        self.remind_password = self.driver.find_element(
            By.CSS_SELECTOR, '.auth-modal__restore-link')
        self.popup_remind_password = self.driver.find_element(
            By.CSS_SELECTOR, '.modal__holder_show_animation')

    def find_social_networks_icons(self):
        self.action.pause(2).perform()
        all_socials_networks_icons = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "socials__list")))
        each_icon_list = all_socials_networks_icons.find_elements(
            By.TAG_NAME, "li")

        return each_icon_list
