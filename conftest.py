import pytest
from selenium import webdriver
from locators.base_page_locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import main_page_url


# В рамках подготовки к тестам - запуск браузера Firefox, ожидание загрузки страницы и принятие кук сайта.
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(main_page_url)
    yield driver
    driver.quit()