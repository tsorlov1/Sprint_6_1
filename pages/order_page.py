import allure
from selenium.webdriver import Keys
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Ожидание загрузки страницы "Для кого самокат"')
    def wait_order_form(self):
        self.wait_for_visibility_of_element(OrderPageLocators.ORDER_FORM_NAME)

    @allure.step('Заполнение поля "Имя"')
    def set_name(self, name):
        self.send_keys(OrderPageLocators.FIRS_NAME_FIELD, name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_lastname(self, lastname):
        self.send_keys(OrderPageLocators.LAST_NAME_FIELD, lastname)

    @allure.step('Заполнение поля "Адрес"')
    def set_address(self, address):
        self.send_keys(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step('Нажать на поле "Станция метро"')
    def click_metro_station_field(self):
        self.click_element(OrderPageLocators.METRO_STATION_FIELD)

    @allure.step('Выбор станции метро из списке')
    def choice_metro_station(self, metro):
        self.scroll(metro)
        self.wait_for_element_to_be_clickable(metro)
        self.click_element(metro)

    @allure.step('Заполнение поля "Телефон"')
    def set_phone(self, phone):
        self.send_keys(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step('Заполнение формы "Для кого самокат"')
    def fill_order_form(self, firstname, lastname, address, metro, phone):
        self.wait_order_form()
        self.set_name(firstname)
        self.set_lastname(lastname)
        self.set_address(address)
        self.click_metro_station_field()
        self.choice_metro_station(metro)
        self.set_phone(phone)

    @allure.step('Нажать кнопку "Далее" в форме "Для кого самокат"')
    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Ожидание загрузки формы "Про аренду"')
    def wait_rent_form(self):
        self.wait_for_visibility_of_element(OrderPageLocators.RENT_FORM_NAME)

    @allure.step('Заполнение поля "Дата аренды"')
    def set_rent_date_field(self, rent_date):
        self.send_keys(OrderPageLocators.RENT_DATE_FIELD, rent_date)
        self.send_keys(OrderPageLocators.RENT_DATE_FIELD, Keys.ENTER)

    @allure.step('Нажать на поле "Срок аренды"')
    def click_rent_period_field(self):
        self.click_element(OrderPageLocators.RENT_PERIOD_FIELD)

    @allure.step('Выбор срока аренды')
    def click_amount_days(self, amount_days):
        self.click_element(amount_days)

    @allure.step('Выбор цвета самоката')
    def click_colour_scooter(self, colour_scooter):
        self.click_element(colour_scooter)

    @allure.step('Заполнение поля "Комментарий для курьера"')
    def set_comment(self, comment):
        self.send_keys(OrderPageLocators.COMMENT_FIELD, comment)

    @allure.step('Заполнение формы "Про аренду"')
    def fill_rent_form(self, rent_date, amount_days, colour_scooter, comment):
        self.wait_rent_form()
        self.set_rent_date_field(rent_date)
        self.click_rent_period_field()
        self.click_amount_days(amount_days)
        self.click_colour_scooter(colour_scooter)
        self.set_comment(comment)

    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Ожидание загрузки окна "Хотите оформить заказ?"')
    def wait_popup_order(self):
        self.wait_for_visibility_of_element(OrderPageLocators.POPUP_ORDER)

    @allure.step('Нажать кнопку "Да" в окне "Хотите оформить заказ?"')
    def click_popup_yes_button(self):
        self.click_element(OrderPageLocators.POPUP_YES_BUTTON)

    @allure.step('Проверка появления окна создания заказа с кнопкой "Посмотреть статус"')
    def check_order_create_window(self):
        self.wait_for_visibility_of_element(OrderPageLocators.POPUP_STATUS_BUTTON)
        current_text = self.get_current_text(OrderPageLocators.POPUP_STATUS_BUTTON)
        assert current_text == 'Посмотреть статус', 'Окно создания заказа с кнопкой "Посмотреть статус" не появилось'



