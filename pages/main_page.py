import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import *
from locators.base_page_locators import *
from conftest import *


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    
    @allure.step('Клик по кнопке "Заказать"')
    def click_main_page_order_button(self):
        self.driver.find_element(*main_page_order_button).click()


    @allure.step('Скролл до блока FAQ')
    def scroll_to_faq(self):
        faq_header = self.driver.find_element(*faq_panel_header)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", faq_header)


    @allure.step('Клик по вопросу в блоке FAQ')
    def click_faq_button(self, faq_question):
        faq_question_text = accordion_button(faq_question)
        self.driver.find_element(*faq_question_text).click()


    @allure.step('Ожидание загрузки панели FAQ')
    def wait_for_load_faq_panel(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(accordion_panel))


    @allure.step('Получение ответа на вопрос из блока FAQ')
    def check_faq_answer(self):
        faq_answers_text = self.driver.find_elements(*accordion_panel)
        for faq_answer_text in faq_answers_text:
            if faq_answer_text.is_displayed():
                return faq_answer_text.text



    