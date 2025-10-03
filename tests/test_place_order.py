import allure
from locators.base_page_locators import *
from pages.order_page import *
from pages.main_page import *
from datasets import *


class TestPlaceOrder:

    @allure.title('Проверка возможности создания заказа')
    @pytest.mark.parametrize("customer_info", customer_list)
    def test_place_order_success(self, driver, customer_info):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)

        main_page.click_main_page_order_button()
        order_page.wait_for_load_order_page()
        order_page.fill_first_order_page(customer_info['name'], customer_info['surname'], customer_info['address'], 
                                         customer_info['station_name'], customer_info['phone_number'])
        order_page.fill_second_order_page(customer_info['order_date'], customer_info['rent_time'], customer_info['color'])
        order_page.wait_for_load_confirm_modal()
        order_page.click_confirm_button()
        order_page.wait_for_load_order_number_modal()


        assert "Заказ оформлен" in order_page.check_order_number_modal_text()