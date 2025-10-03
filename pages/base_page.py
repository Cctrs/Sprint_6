import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import *
from conftest import *


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    
    @allure.step('Клик по логотипу Яндекса, переключение на новую вкладку, ожидание загрузки хедера дзена')
    def click_yandex_logo(self):
        self.driver.find_element(*yandex_logo).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        all_windows = self.driver.window_handles
        new_window = all_windows[1]
        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(dzen_header))


    @allure.step('Клик по логотипу Самоката, переход на главную, ожидание загрузки страницы')
    def click_scooter_logo(self):
        self.driver.find_element(*scooter_logo).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(scooter_picture_area))
