import time

import pytest
from selenium.webdriver.common.by import By
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
    chrome.get('https://ultimateqa.com/complicated-page/')
    button = chrome.find_element(By.XPATH, '//*[@id="post-579"]/div/div[1]/div/div/div[3]/div[2]/div[2]/a')
    button.click()
    time.sleep(5)


def test_2(browser):
    chrome = browser
    chrome.implicitly_wait(10)
    chrome.get('https://ultimateqa.com/complicated-page/')
    button = chrome.find_element(By.CSS_SELECTOR, '[class="et_pb_button et_pb_button_4 et_pb_bg_layout_light"]')
    button.click()
    time.sleep(5)


def test_3(browser):
    chrome = browser
    chrome.implicitly_wait(10)
    chrome.get('https://ultimateqa.com/complicated-page/')
    button = chrome.find_element(By.CLASS_NAME, 'et_pb_button et_pb_button_4 et_pb_bg_layout_light')
    button.click()
    time.sleep(5)
