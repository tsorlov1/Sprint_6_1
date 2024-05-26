import pytest
import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from config import TextAnswer


class TestQuestionList:
    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном» на соответствие вопрос-ответ в браузере Сhrome')
    @allure.description('При нажатии на вопрос открывается соответствующий ему ответ')
    @pytest.mark.parametrize(
        'question,answer,text_answer',
        [
            [MainPageLocators.QUESTION_PRICE, MainPageLocators.ANSWER_PRICE, TextAnswer.text_answer_price],
            [MainPageLocators.QUESTION_MANY_SCOOTERS, MainPageLocators.ANSWER_MANY_SCOOTERS, TextAnswer.text_answer_many_scooters],
            [MainPageLocators.QUESTION_RENTAL_PERIOD, MainPageLocators.ANSWER_RENTAL_PERIOD, TextAnswer.text_answer_rental_period],
            [MainPageLocators.QUESTION_SCOOTER_TODAY, MainPageLocators.ANSWER_SCOOTER_TODAY, TextAnswer.text_answer_scooter_today],
            [MainPageLocators.QUESTION_PROLONG_OR_RETURN, MainPageLocators.ANSWER_PROLONG_OR_RETURN, TextAnswer.text_answer_prolong_or_return],
            [MainPageLocators.QUESTION_CHARGING, MainPageLocators.ANSWER_CHARGING, TextAnswer.text_answer_charging],
            [MainPageLocators.QUESTION_CANCEL_ORDER, MainPageLocators.ANSWER_CANCEL_ORDER, TextAnswer.text_answer_cancel_order],
            [MainPageLocators.QUESTION_DELIVERY_AREA, MainPageLocators.ANSWER_DELIVERY_AREA, TextAnswer.text_answer_delivery_area]
        ]
    )
    def test_question_list_сhrome(self, driver_сhrome, question, answer, text_answer):
        main_page = MainPage(driver_сhrome)
        main_page.click_question_button(question)
        main_page.check_answer_text(answer, text_answer)

    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном» на соответствие вопрос-ответ в браузере Firefox')
    @allure.description('При нажатии на вопрос открывается соответствующий ему ответ')
    @pytest.mark.parametrize(
        'question,answer,text_answer',
        [
            [MainPageLocators.QUESTION_PRICE, MainPageLocators.ANSWER_PRICE, TextAnswer.text_answer_price],
            [MainPageLocators.QUESTION_MANY_SCOOTERS, MainPageLocators.ANSWER_MANY_SCOOTERS,
             TextAnswer.text_answer_many_scooters],
            [MainPageLocators.QUESTION_RENTAL_PERIOD, MainPageLocators.ANSWER_RENTAL_PERIOD,
             TextAnswer.text_answer_rental_period],
            [MainPageLocators.QUESTION_SCOOTER_TODAY, MainPageLocators.ANSWER_SCOOTER_TODAY,
             TextAnswer.text_answer_scooter_today],
            [MainPageLocators.QUESTION_PROLONG_OR_RETURN, MainPageLocators.ANSWER_PROLONG_OR_RETURN,
             TextAnswer.text_answer_prolong_or_return],
            [MainPageLocators.QUESTION_CHARGING, MainPageLocators.ANSWER_CHARGING, TextAnswer.text_answer_charging],
            [MainPageLocators.QUESTION_CANCEL_ORDER, MainPageLocators.ANSWER_CANCEL_ORDER,
             TextAnswer.text_answer_cancel_order],
            [MainPageLocators.QUESTION_DELIVERY_AREA, MainPageLocators.ANSWER_DELIVERY_AREA,
             TextAnswer.text_answer_delivery_area]
        ]
    )
    def test_question_list_firefox(self, driver_firefox, question, answer, text_answer):
        main_page = MainPage(driver_firefox)
        main_page.click_question_button(question)
        main_page.check_answer_text(answer, text_answer)
