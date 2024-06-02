import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import url_scooter, url_dzen

class MainPage(BasePage):

    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button(self, locator):
        self.scroll(locator)
        self.wait_for_element_to_be_clickable(locator)
        self.click_element(locator)

    @allure.step('Нажать на логотип "Самокат"')
    def click_logo_scooter(self):
        self.click_order_button(MainPageLocators.ORDER_BUTTON_HEADER)
        self.wait_for_element_to_be_clickable(MainPageLocators.SCOOTER_LOGO)
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Нажать на логотип "Яндекс"')
    def click_logo_yandex(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.YANDEX_LOGO)
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Проверить URL страницы после нажатия на логотип "Самокат"')
    def check_page_scooter(self):
        current_url = self.get_current_url()
        assert current_url == url_scooter

    @allure.step('Проверить URL страницы после нажатия на логотип "Яндекс"')
    def check_page_dzen(self):
        current_url = self.get_current_url()
        assert current_url == url_dzen

    @allure.step('При нажатии на логотип "Яндекс", в новом окне через редирект открывается главная страница "Дзен"')
    def go_dzen(self):
        self.switch_to_window()
        self.wait_for_visibility_of_element(MainPageLocators.DZEN_LOGO)

    @allure.step('Нажать на вопрос в разделе "Вопросы о важном"')
    def click_question_button(self, locator):
        self.scroll(locator)
        self.wait_for_element_to_be_clickable(locator)
        self.click_element(locator)

    @allure.step('Проверка соответствия ответа выбранному вопросу')
    def check_answer_text(self, answer, text_answer):
        self.wait_for_visibility_of_element(answer)
        current_text = self.get_current_text(answer)
        assert current_text == text_answer

