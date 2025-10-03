import allure
from locators.main_page_locators import *
from pages.main_page import *
from datasets import faq_list


class TestFaq:

    @allure.title('Проверка соответствия ответов на вопросы из FAQ')
    @pytest.mark.parametrize("faq_data", faq_list)
    def test_faq_answer_corresponds_faq_question(self, driver, faq_data):
        main_page = MainPage(driver)

        main_page.scroll_to_faq()
        main_page.click_faq_button(faq_data['question'])
    

        assert main_page.check_faq_answer() == faq_data['answer']