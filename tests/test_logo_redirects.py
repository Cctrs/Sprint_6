import allure
from locators.base_page_locators import *
from pages.base_page import *
from pages.main_page import *


class TestLogoRedirects:

    @allure.title('Проверка редиректа на главную страницу сайта по клику на название "Самокат"')
    def test_scooter_logo_redirects_on_main_page(self, driver):
        main_page = MainPage(driver)
        default_page = BasePage(driver)

        main_page.click_main_page_order_button()
        default_page.click_scooter_logo()

        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'


    @allure.title('Проверка редиректа на главную страницу dzen.ru по клику на название "Яндекс"')
    def test_yandex_logo_redirects_on_dzen(self, driver):
        default_page = BasePage(driver)

        default_page.click_yandex_logo()

        assert 'https://dzen.ru/' in driver.current_url
