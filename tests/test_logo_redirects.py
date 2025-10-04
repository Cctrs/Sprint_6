import allure
from pages.main_page import *
from urls import *


class TestLogoRedirects:

    @allure.title('Проверка редиректа на главную страницу сайта по клику на название "Самокат"')
    def test_scooter_logo_redirects_on_main_page(self, driver):
        main_page = MainPage(driver)

        main_page.click_main_page_order_button()
        main_page.click_element(scooter_logo)
        main_page.wait_element_for_load(scooter_picture_area)

        assert main_page.get_current_url() == main_page_url


    @allure.title('Проверка редиректа на главную страницу dzen.ru по клику на название "Яндекс"')
    def test_yandex_logo_redirects_on_dzen(self, driver):
        main_page = MainPage(driver)

        main_page.click_element(yandex_logo)
        main_page.switch_to_new_window()
        main_page.wait_element_for_load(dzen_header)

        assert dzen_mane_page_url in main_page.get_current_url()
