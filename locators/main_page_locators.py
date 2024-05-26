from selenium.webdriver.common.by import By

class MainPageLocators:
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    DZEN_LOGO = (By.CLASS_NAME, 'desktop-base-header__logoLink-2h')
    QUESTION_PRICE = (By.ID, 'accordion__heading-0')  # вопрос 1 "Сколько это стоит? и как оплатить?"
    ANSWER_PRICE = (By.ID, 'accordion__panel-0')  # ответ на 1 вопрос
    QUESTION_MANY_SCOOTERS = (By.ID, 'accordion__heading-1')  # вопрос 2 "Хочу сразу несколько самокатов! Так можно?"
    ANSWER_MANY_SCOOTERS = (By.ID, 'accordion__panel-1')  # ответ на 2 вопрос
    QUESTION_RENTAL_PERIOD = (By.ID, 'accordion__heading-2')  # вопрос 3 "Как рассчитывается время аренды?"
    ANSWER_RENTAL_PERIOD = (By.ID, 'accordion__panel-2')  # ответ на 3 вопрос
    QUESTION_SCOOTER_TODAY = (By.ID, 'accordion__heading-3')  # вопрос 4 "Можно ли заказать самокат прямо на сегодня?"
    ANSWER_SCOOTER_TODAY = (By.ID, 'accordion__panel-3')  # ответ на 4 вопрос
    QUESTION_PROLONG_OR_RETURN = (By.ID, 'accordion__heading-4')  # вопрос 5 "Можно ли продлить заказ или вернуть самокат раньше?"
    ANSWER_PROLONG_OR_RETURN = (By.ID, 'accordion__panel-4')  # ответ на 5 вопрос
    QUESTION_CHARGING = (By.ID, 'accordion__heading-5')  # вопрос 6 "Вы привозите зарядку вместе с самокатом?"
    ANSWER_CHARGING = (By.ID, 'accordion__panel-5')  # ответ на 6 вопрос
    QUESTION_CANCEL_ORDER = (By.ID, 'accordion__heading-6')  # вопрос 7 "Можно ли отменить заказ?"
    ANSWER_CANCEL_ORDER = (By.ID, 'accordion__panel-6')  # ответ на 7 вопрос
    QUESTION_DELIVERY_AREA = (By.ID, 'accordion__heading-7')  # вопрос 8 "Я жизу за МКАДом, привезёте?"
    ANSWER_DELIVERY_AREA = (By.ID, 'accordion__panel-7')  # ответ на 8 вопрос
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')  # логотип "Яндекс" в шапке сайта
    ORDER_BUTTON_HEADER = (By.CLASS_NAME, 'Button_Button__ra12g')  # кнопка "Заказать" в шапке сайта
    ORDER_BUTTON_PAGE = (By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button')  # кнопка "Заказать" на странице сайта


