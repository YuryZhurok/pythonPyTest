import time

import pytest
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_1(browser):
    chrome = browser
    chrome.implicitly_wait(10)
    chrome.get('https://thedemosite.co.uk/savedata.php')
    inputs_username = chrome.find_element(By.CSS_SELECTOR, '[name="username"]')
    inputs_username.send_keys('fdgghgfhgf')
    inputs_password = chrome.find_element(By.CSS_SELECTOR, '[type ="password"]')
    inputs_password.send_keys('dfgdfg')
    button = chrome.find_element(By.CSS_SELECTOR, '[type ="button"]')
    button.click()
    time.sleep(10)


def test_2(browser):
    chrome = browser
    chrome.implicitly_wait(10)
    chrome.get('https://demoqa.com/text-box')
    inputs_name = chrome.find_element(By.CSS_SELECTOR, '[placeholder="Full Name"]')
    inputs_name.send_keys('Yury')
    inputs_email = chrome.find_element(By.CSS_SELECTOR, '[type="email"]')
    inputs_email.send_keys('yury@gmail.com')
    inputs_current_address = chrome.find_element(By.CSS_SELECTOR, '[placeholder="Current Address"]')
    inputs_current_address.send_keys('Minsk, Komsomolskaya 20')
    inputs_perm_adr = chrome.find_element(By.XPATH, '//div[@class="text-field-container"]/form/div[4]/div[2]/textarea')
    inputs_perm_adr.send_keys('Minsk, Komsomolskaya 20')
    button = chrome.find_element(By.XPATH, '//button[@id="submit"]')
    button.click()
    time.sleep(10)

