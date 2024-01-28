import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class BasePage:
    def __init__(self):
        self.driver = uc.Chrome()

    def close(self):
        self.driver.close()