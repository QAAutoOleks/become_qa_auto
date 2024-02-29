import undetected_chromedriver as uc


class BasePage:
    def __init__(self):
        self.driver = uc.Chrome()

    def close(self):
        self.driver.close()