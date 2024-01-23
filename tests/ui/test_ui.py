import pytest


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.get("https://github.com/login")
    login_element = driver.find_element(By.ID, 'login_field')
    login_element.send_keys('wrong.data@mail.com')

    driver.close()