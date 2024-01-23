import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.get("https://github.com/login")
    login_element = driver.find_element(By.ID, 'login_field')
    login_element.send_keys('wrong.data@mail.com')
    time.sleep(2)
    login_element = driver.find_element(By.ID, 'password')
    login_element.send_keys('wrong_password')
    time.sleep(2)
    button_element = driver.find_element(By.NAME, 'commit')
    button_element.click()
    time.sleep(2)
    assert driver.title == 'Sign in to GitHub · GitHub'

    driver.close()