import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from config import url_scooter, url_dzen


class TestClickLogo:
    @allure.title('Тест. Переход на страницу "Яндекс Самокат" по нажатии на логотип "Самокат" в браузере Сhrome')
    @allure.description('Нажать на логотип "Самокат", откроется страница "Яндекс Самокат"')
    def test_click_logo_scooter_сhrome(self, driver_сhrome):
        main_page = MainPage(driver_сhrome)
        main_page.click_order_button(MainPageLocators.ORDER_BUTTON_HEADER)
        main_page.click_logo(MainPageLocators.SCOOTER_LOGO)
        main_page.check_page(url_scooter)

    @allure.title('Тест. Переход на страницу "Дзен" по нажатии на логотип "Яндекс" в браузере Сhrome')
    @allure.description('Нажать на логотип  "Яндекс", откроется главная страница "Дзен" через редирект')
    def test_click_logo_yandex_сhrome(self, driver_сhrome):
        main_page = MainPage(driver_сhrome)
        main_page.click_logo(MainPageLocators.YANDEX_LOGO)
        main_page.go_dzen()
        main_page.wait_for_visibility_of_element(MainPageLocators.DZEN_LOGO)
        main_page.check_page(url_dzen)

    @allure.title('Тест. Переход на страницу "Яндекс Самокат" по нажатии на логотип "Самокат" в браузере Firefox')
    @allure.description('Нажать на логотип "Самокат", откроется страница "Яндекс Самокат"')
    def test_click_logo_scooter_firefox(self, driver_firefox):
        main_page = MainPage(driver_firefox)
        main_page.click_order_button(MainPageLocators.ORDER_BUTTON_HEADER)
        main_page.click_logo(MainPageLocators.SCOOTER_LOGO)
        main_page.check_page(url_scooter)

    @allure.title('Тест. Переход на страницу "Дзен" по нажатии на логотип "Яндекс" в браузере Firefox')
    @allure.description('Нажать на логотип  "Яндекс", откроется главная страница "Дзен" через редирект')
    def test_click_logo_yandex_firefox(self, driver_firefox):
        main_page = MainPage(driver_firefox)
        main_page.click_logo(MainPageLocators.YANDEX_LOGO)
        main_page.go_dzen()
        main_page.wait_for_visibility_of_element(MainPageLocators.DZEN_LOGO)
        main_page.check_page(url_dzen)