import random

import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import LogInMainPageLocators, LogInPage, PageRegistration

r = random.Random()
faker = Faker()


class GenerateTestData:
    def __init__(self):
        self._random_number = r.randint(100, 999)
        self._password_positive = faker.password(length=6)
        self._password_negative_for_unit = faker.password(length=5)

    def generate_email(self):
        return f'Andrey_Busyrev_18_{str(self._random_number)}@yandex.ru'

    def generate_password(self):
        return self._password_positive

    def generate_password_negative(self):
        return self._password_negative_for_unit

    @staticmethod
    def generate_name():
        return faker.name()


class Helpers:

    def wait_until_visibility_of_element_located(self, driver, locator):
        """
        Ожидаем пока не появится элемент на странице
        :param driver: Браузер
        :param locator: XPATH локатор
        :return:
        """
        return WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, locator)))


@pytest.fixture(scope='function')
def registration(driver, helpers):
    # Переходим на главную страницу
    url = 'https://stellarburgers.nomoreparties.site/'
    driver.get(url)

    # Ожидаем появлния кнопки "Войти в аккаунт"
    helpers.wait_until_visibility_of_element_located(driver, LogInMainPageLocators.LOG_IN_BUTTON)

    # Нажимаем на кнопку "Войти в аккаунт"
    driver.find_element(By.XPATH, LogInMainPageLocators.LOG_IN_BUTTON).click()

    # Ожидаем появления ссылки "Зарегистрироваться"
    helpers.wait_until_visibility_of_element_located(driver, LogInPage.REGISTRATION_LINK)

    # Нажимаем на линк "Зарегистрироваться"
    driver.find_element(By.XPATH, LogInPage.REGISTRATION_LINK).click()

    # Ожидаем появления полей для ввода
    helpers.wait_until_visibility_of_element_located(driver, PageRegistration.INPUT_NAME_EMAIL_PASSWORD)


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture(scope='function')
def helpers():
    helper = Helpers()
    return helper
