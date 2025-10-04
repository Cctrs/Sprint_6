from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import *


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    
    def click_element(self, locator):
        self.driver.find_element(*locator).click()


    def find_all_elements(self, locator):
        return self.driver.find_elements(*locator)


    def wait_element_for_load(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        all_windows = self.driver.window_handles
        new_window = all_windows[1]
        self.driver.switch_to.window(new_window)


    def wait_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))


    def send_keys(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)


    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)


    def get_current_url(self):
        return self.driver.current_url
