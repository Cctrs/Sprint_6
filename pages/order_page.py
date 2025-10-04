import allure
from locators.order_page_locators import *
from locators.base_page_locators import *
from conftest import *
from pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Ожидание загрузки страницы заказа')
    def wait_for_load_order_page(self):
        self.wait_element_for_load(next_button)


    @allure.step('Заполнение поля имя')
    def add_name(self, name):
        self.send_keys(name_input, name)

    
    @allure.step('Заполнение поля фамилия')
    def add_surname(self, surname):
        self.send_keys(surname_input, surname)


    @allure.step('Заполнение поля адрес')
    def add_address(self, address):
        self.send_keys(address_input, address)

    
    @allure.step('Заполнение поля станция метро')
    def add_metro_station(self, station_name):
        self.send_keys(metro_station_input, station_name)
        metro_station_name = metro_station_dropdown_select(station_name)
        self.click_element(metro_station_name)

    
    @allure.step('Заполнение поля номер телефона')
    def add_phone_number(self, phone_number):
        self.send_keys(phone_number_input, phone_number)


    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        self.click_element(next_button)


    @allure.step('Заполнение первой страницы заказа')
    def fill_first_order_page(self, name, surname, address, station_name, phone_number):
        self.add_name(name)
        self.add_surname(surname)
        self.add_address(address)
        self.add_metro_station(station_name)
        self.add_phone_number(phone_number)
        self.click_next_button()

    
    @allure.step('Ожидание загрузки второй страницы заказа')
    def wait_for_load_second_order_page(self):
        self.wait_element_for_load(order_button)

    
    @allure.step('Выбор даты заказа')
    def add_date(self, order_date):
        self.click_element(date_input)
        day_number = date_in_calendar(order_date)
        self.click_element(day_number)

    
    @allure.step('Выбор длительности заказа')
    def add_rent_time(self, rent_time):
        self.click_element(rent_time_input)
        rent_time_amount = rent_time_amount_select(rent_time)
        self.click_element(rent_time_amount)


    @allure.step('Выбор цвета самоката')
    def choose_scooter_color(self, color):
        if color == 'black':
            self.click_element(black_scooter)
        else:
            self.click_element(grey_scooter)
    

    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button(self):
        self.click_element(order_button)


    @allure.step('Заполнение второй страницы заказа')
    def fill_second_order_page(self, order_date, rent_time, color):
        self.add_date(order_date)
        self.add_rent_time(rent_time)
        self.choose_scooter_color(color)
        self.click_order_button()
    

    @allure.step('Ожидание загрузки окна подтверждения заказа')
    def wait_for_load_confirm_modal(self):
        self.wait_element_to_be_clickable(confirm_button)

    
    @allure.step('Клик по кнопке подтверждения')
    def click_confirm_button(self):
        self.click_element(confirm_button)


    @allure.step('Ожидания модального окна с номером заказа')
    def wait_for_load_order_number_modal(self):
        self.wait_element_for_load(order_number_modal)

    
    @allure.step('Получение заголовка окна с номером заказа')
    def check_order_number_modal_text(self):
        order_number_modal_text = self.find_one_element(order_number_modal).text
        return order_number_modal_text
