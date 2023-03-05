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
    chrome.get('https://ultimateqa.com/filling-out-forms/')
    input_name = chrome.find_element(By.ID, 'et_pb_contact_name_0')
    input_name.send_keys('Yury')
    input_message = chrome.find_element(By.ID, 'et_pb_contact_message_0')
    input_message.send_keys('Hello')
    time.sleep(5)
    button_submit = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_form_0"]/div[2]/form/input[1]')
    button_submit.submit()
    find_message = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_form_0"]/div/p')
    find_message.is_displayed()
    time.sleep(10)


def test_2(browser):
    chrome = browser
    chrome.implicitly_wait(10)
    chrome.get('https://ultimateqa.com/filling-out-forms/')
    input_name = chrome.find_element(By.ID, 'et_pb_contact_name_0')
    input_name.send_keys('Yury')
    time.sleep(5)
    button_submit = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_form_0"]/div[2]/form/input[1]')
    button_submit.submit()
    find_message = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_form_0"]/div[1]/p')
    find_message.is_displayed()
    time.sleep(10)


def test_3(browser):
    chrome = browser
    chrome.implicitly_wait(10)
    chrome.get('https://ultimateqa.com/filling-out-forms/')
    input_message = chrome.find_element(By.ID, 'et_pb_contact_message_0')
    input_message.send_keys('Hello')
    time.sleep(5)
    button_submit = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_form_0"]/div[2]/form/input[1]')
    button_submit.submit()
    find_message = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_form_0"]/div[1]/p')
    find_message.is_displayed()
    time.sleep(10)

