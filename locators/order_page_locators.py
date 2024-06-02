from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_FORM_NAME = (By.CLASS_NAME, 'Order_Header__BZXOb')  # имя формы заказа "Для кого самокат"
    FIRS_NAME_FIELD = (By.CSS_SELECTOR, '[placeholder="* Имя"]')  # Поле "Имя"
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '[placeholder="* Фамилия"]')  # Поле "Фамилия"
    ADDRESS_FIELD = (By.CSS_SELECTOR, '[placeholder="* Адрес: куда привезти заказ"]')  # Поле "Адрес: Куда привезти заказ"
    METRO_STATION_FIELD = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')  # Поле "Станция метро"
    LIST_METRO_STATIONS = [By.XPATH, '//li[@data-value="1"]']
    METRO_SOKOLNIKI = (By.XPATH, '//div[text()="Сокольники"]')  # Станция метро "Сокольники"
    METRO_CHISTIE_PRUDI = (By.XPATH, '//div[text()="Чистые пруды"]')  # Станция метро "Чистые пруды"
    PHONE_FIELD = (By.CSS_SELECTOR, '[placeholder="* Телефон: на него позвонит курьер"]')  # Поле "Телефон: на него позвонит курьер"
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')  # Кнопка "Далее"
    RENT_FORM_NAME = (By.CLASS_NAME, 'Order_Header__BZXOb')  # имя формы заказа "Про аренду"
    RENT_DATE_FIELD = (By.CSS_SELECTOR, '[placeholder="* Когда привезти самокат"]')  # Поле "Когда привезти самокат"
    RENT_PERIOD_FIELD = (By.CLASS_NAME, 'Dropdown-placeholder')  # Поле "Срок аренды"
    ONE_DAY_PERIOD = (By.XPATH, '//div[text() = "сутки"]')  # выпадающий список срока аренды "сутки"
    SEVEN_DAY_PERIOD = (By.XPATH, '//div[text() = "семеро суток"]')  # выпадающий список срока аренды "четверо суток"
    SCOOTER_COLOUR_BLACK = (By.ID, 'black')  # чек-бокс цвета самоката "чёрный"
    SCOOTER_COLOUR_GRAY = (By.ID, 'grey')  # чек-бокс цвета самоката "серый"
    COMMENT_FIELD = (By.CSS_SELECTOR, '[placeholder="Комментарий для курьера"]')  # Поле "Комментарий для курьера"
    ORDER_BUTTON = (By.XPATH, '//div[@class = "Order_Buttons__1xGrp"]/button[text()="Заказать"]')  # Кнопка "заказать"
    POPUP_ORDER = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')  # поп-ап "Хотите оформить заказ?"
    POPUP_YES_BUTTON = (By.XPATH, '//button[text()="Да"]')  # Кнопка "Да" в поп-апе "Хотите оформить заказ?"
    POPUP_STATUS_BUTTON = (By.XPATH, '//button[text()="Посмотреть статус"]')  # Кнопка "Посмотреть статус" в форме "Заказ оформлен"
    LOGO_SCOOTER = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')  # Логотип "Самокат"