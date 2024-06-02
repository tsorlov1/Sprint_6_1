import pytest
import allure
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage
from pages.main_page import MainPage

@allure.feature('Заказ самоката')
class TestScooterOrder:

    @allure.title('Тест. Заказа самоката в браузере Chrome')
    @allure.description(
        'Нажать на кнопку "Заказать", заполнить формы "Для кого самокат" и "Про аренду", дождаться окно "Посмотреть статус"'
    )
    @pytest.mark.parametrize(
        'order_button, first_name, last_name, address, metro, phone, rent_date, amount_days, colour_scooter, comment',
        [
            [MainPageLocators.ORDER_BUTTON_HEADER , 'Ян', 'Го', 'Никольская, 1', OrderPageLocators.METRO_SOKOLNIKI, '79009009090',
             '26.05.2024', OrderPageLocators.ONE_DAY_PERIOD, OrderPageLocators.SCOOTER_COLOUR_BLACK, ''],
            [MainPageLocators.ORDER_BUTTON_HEADER , 'Габдельмуталлип', 'Александрийский', 'Бакинских Комиссаров 26-ти, улица 3 к3 с1А', OrderPageLocators.METRO_SOKOLNIKI, '89009009090',
             '30.05.2024', OrderPageLocators.SEVEN_DAY_PERIOD, OrderPageLocators.SCOOTER_COLOUR_GRAY, 'Позвонить за 15 мин']
        ]
    )
    def test_scooter_orders_сhrome(self, driver_сhrome, order_button, first_name, last_name, address, metro, phone, rent_date, amount_days, colour_scooter, comment):
        main_page = MainPage(driver_сhrome)
        main_page.click_order_button(order_button)
        order_page = OrderPage(driver_сhrome)
        order_page.fill_order_form(first_name, last_name, address, metro, phone)
        order_page.click_next_button()
        order_page.fill_rent_form(rent_date, amount_days, colour_scooter, comment)
        order_page.click_order_button()
        order_page.wait_popup_order()
        order_page.click_popup_yes_button()
        order_page.check_order_create_window()

    @allure.title('Тест. Заказа самоката в браузере Firefox')
    @allure.description(
        'Нажать на кнопку "Заказать", заполнить формы "Для кого самокат" и "Про аренду", дождаться окно "Посмотреть статус"'
    )
    @pytest.mark.parametrize(
        'order_button, first_name, last_name, address, metro, phone, rent_date, amount_days, colour_scooter, comment',
        [
            [MainPageLocators.ORDER_BUTTON_HEADER, 'Ян', 'Го', 'Никольская, 1', OrderPageLocators.METRO_SOKOLNIKI,
             '79009009090',
             '26.05.2024', OrderPageLocators.ONE_DAY_PERIOD, OrderPageLocators.SCOOTER_COLOUR_BLACK, ''],
            [MainPageLocators.ORDER_BUTTON_HEADER, 'Габдельмуталлип', 'Александрийский',
             'Бакинских Комиссаров 26-ти, улица 3 к3 с1А', OrderPageLocators.METRO_SOKOLNIKI, '89009009090',
             '30.05.2024', OrderPageLocators.SEVEN_DAY_PERIOD, OrderPageLocators.SCOOTER_COLOUR_GRAY,
             'Позвонить за 15 мин']
        ]
    )
    def test_scooter_orders_firefox(self, driver_firefox, order_button, first_name, last_name, address, metro, phone, rent_date,
                            amount_days, colour_scooter, comment):
        main_page = MainPage(driver_firefox)
        main_page.click_order_button(order_button)
        order_page = OrderPage(driver_firefox)
        order_page.fill_order_form(first_name, last_name, address, metro, phone)
        order_page.click_next_button()
        order_page.fill_rent_form(rent_date, amount_days, colour_scooter, comment)
        order_page.click_order_button()
        order_page.wait_popup_order()
        order_page.click_popup_yes_button()
        order_page.check_order_create_window()