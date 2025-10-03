import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.order_page_locators import *
from locators.base_page_locators import *
from conftest import *


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание загрузки страницы заказа')
    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(next_button))


    @allure.step('Заполнение поля имя')
    def add_name(self, name):
        self.driver.find_element(*name_input).send_keys(name)

    
    @allure.step('Заполнение поля фамилия')
    def add_surname(self, surname):
        self.driver.find_element(*surname_input).send_keys(surname)


    @allure.step('Заполнение поля адрес')
    def add_address(self, address):
        self.driver.find_element(*address_input).send_keys(address)

    
    @allure.step('Заполнение поля станция метро')
    def add_metro_station(self, station_name):
        self.driver.find_element(*metro_station_input).send_keys(station_name)
        metro_station_name = metro_station_dropdown_select(station_name)
        self.driver.find_element(*metro_station_name).click()

    
    @allure.step('Заполнение поля номер телефона')
    def add_phone_number(self, phone_number):
        self.driver.find_element(*phone_number_input).send_keys(phone_number)


    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        self.driver.find_element(*next_button).click()


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
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(order_button))

    
    @allure.step('Выбор даты заказа')
    def add_date(self, order_date):
        self.driver.find_element(*date_input).click()
        day_number = date_in_calendar(order_date)
        self.driver.find_element(*day_number).click()

    
    @allure.step('Выбор длительности заказа')
    def add_rent_time(self, rent_time):
        self.driver.find_element(*rent_time_input).click()
        rent_time_amount = rent_time_amount_select(rent_time)
        self.driver.find_element(*rent_time_amount).click()


    @allure.step('Выбор цвета самоката')
    def choose_scooter_color(self, color):
        if color == 'black':
            self.driver.find_element(*black_scooter).click()
        else:
            self.driver.find_element(*grey_scooter).click()
    

    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button(self):
        self.driver.find_element(*order_button).click()


    @allure.step('Заполнение второй страницы заказа')
    def fill_second_order_page(self, order_date, rent_time, color):
        self.add_date(order_date)
        self.add_rent_time(rent_time)
        self.choose_scooter_color(color)
        self.click_order_button()
    

    @allure.step('Ожидание загрузки окна подтверждения заказа')
    def wait_for_load_confirm_modal(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(confirm_button))

    
    @allure.step('Клик по кнопке подтверждения')
    def click_confirm_button(self):
        self.driver.find_element(*confirm_button).click()


    @allure.step('Ожидания модального окна с номером заказа')
    def wait_for_load_order_number_modal(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(order_number_modal))

    
    @allure.step('Получение заголовка окна с номером заказа')
    def check_order_number_modal_text(self):
        order_number_modal_text = self.driver.find_element(*order_number_modal).text
        return order_number_modal_text
