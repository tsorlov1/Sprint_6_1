import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button(self, locator):
        self.scroll(locator)
        self.wait_for_element_to_be_clickable(locator)
        self.click_element(locator)

    @allure.step('Нажать на логотип')
    def click_logo(self, locator):
        self.wait_for_element_to_be_clickable(locator)
        self.click_element(locator)

    @allure.step('Проверить URL')
    def check_page(self, url):
        current_url = self.get_current_url()
        assert current_url == url

    @allure.step('При нажатии на логотип "Яндекс", в новом окне через редирект открывается главная страница "Дзен"')
    def go_dzen(self):
        self.switch_to_window()

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

