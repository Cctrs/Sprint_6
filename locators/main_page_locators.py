from selenium.webdriver.common.by import By

faq_panel_header = (By.CLASS_NAME, 'Home_SubHeader__zwi_E')
accordion_button = lambda faq_question: (By.XPATH, f'//div[text()="{faq_question}"]')
accordion_panel = (By.XPATH, '//div[@class="accordion__panel"]')
main_page_order_button = (By.XPATH, '//button[text()="Заказать"]')