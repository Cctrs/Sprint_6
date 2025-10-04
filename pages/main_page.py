import allure
from locators.main_page_locators import *
from locators.base_page_locators import *
from conftest import *
from base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Ожидание загрузки главной страницы')
    def wait_main_page_for_load(self):
        self.wait_element_for_load(main_page_order_button)


    @allure.step('Клип по кнопке принятия куки')
    def cookie_accept(self):
        self.click_element(accept_cookies_button)


    @allure.step('Клик по кнопке "Заказать"')
    def click_main_page_order_button(self):
        self.click_element(main_page_order_button)


    @allure.step('Скролл до блока FAQ')
    def scroll_to_faq(self):
        self.scroll_to_element(faq_panel_header)


    @allure.step('Клик по вопросу в блоке FAQ')
    def click_faq_button(self, faq_question):
        faq_question_text = accordion_button(faq_question)
        self.click_element(faq_question_text)


    @allure.step('Ожидание загрузки панели FAQ')
    def wait_for_load_faq_panel(self):
        self.wait_element_for_load(accordion_panel)


    @allure.step('Получение ответа на вопрос из блока FAQ')
    def check_faq_answer(self):
        faq_answers_text = self.find_all_elements(accordion_panel)
        for faq_answer_text in faq_answers_text:
            if faq_answer_text.is_displayed():
                return faq_answer_text.text



    