import pytest
from selenium import webdriver

@pytest.fixture
def driver_сhrome():
    driver = webdriver.Chrome()
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield  driver
    driver.quit()

@pytest.fixture
def driver_firefox():
    driver = webdriver.Firefox()
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield  driver
    driver.quit()
