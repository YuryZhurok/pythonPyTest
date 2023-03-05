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
    chrome.get('https://baraholka.onliner.by/')
    find_button = chrome.find_element(By.XPATH, '//a[@class="b-btn-fleamarket__1"]')
    time.sleep(5)


def test_2(browser):
    chrome = browser
    chrome.implicitly_wait(10)
    chrome.get('https://baraholka.onliner.by/')
    find_button = chrome.find_element(By.CSS_SELECTOR, 'div.b-columntopic.columntopic-bah div:nth-child(1) '
                                                       '\ndiv:nth-child(2) ul li:nth-child(9) sup')
    time.sleep(5)


def test_3(browser):
    chrome = browser
    chrome.implicitly_wait(10)
    chrome.get('https://baraholka.onliner.by/')
    find_button = chrome.find_element(By.CSS_SELECTOR, 'div.b-columntopic.columntopic-bah div:nth-child(2) '
                                                       '\ndiv:nth-child(2) ul li:nth-child(5) sup')
    time.sleep(5)

