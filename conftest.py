import random

import pytest
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
