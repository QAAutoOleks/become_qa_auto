import os
from platform import system
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



class BasePage:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        exec_path = os.path.join(os.getcwd(), 'driver', 'chromedriver.exe') if system() == "Windows" else \
            os.path.join(os.getcwd(), 'driver', 'chromedriver')
        driver = webdriver.Chrome(options=options, service=Service(log_path=os.devnull, executable_path=exec_path))
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        'source': '''
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
        '''
        })

    def close(self):
        self.driver.close()