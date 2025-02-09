import random
from faker import Faker

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src import constants

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

    def get_text_from_element(self, driver, locator):
        """
        Получаем тест из элемента
        :param driver:
        :param locator:
        :return:
        """
        return driver.find_element(By.XPATH, locator).text


class CreateUser:

    def __init__(self, name, mail, password):
        self.name = name
        self.email = mail
        self.password = password

    @classmethod
    def generate_user(cls):
        generator = GenerateTestData()
        return cls(generator.generate_name(), generator.generate_email(), generator.generate_password())

    def user_registration(self, driver, helpers):
        registration(driver, helpers)
        fields_input = driver.find_elements(By.XPATH, PageRegistration.INPUT_NAME_EMAIL_PASSWORD)
        fields_input[0].send_keys(self.name)
        fields_input[1].send_keys(self.email)
        fields_input[2].send_keys(self.password)
        driver.find_element(By.XPATH, PageRegistration.REGISTRATION_BUTTON).click()

        return self.email, self.password


def registration(driver, helpers):
    # Переходим на главную страницу
    driver.get(constants.BASE_URL)

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


def authoriztaion(driver, email, password):
    # Заполняем данные зарегистрированным пользователем
    driver.find_element(By.XPATH, LogInPage.INPUT_EMAIL).send_keys(email)
    driver.find_element(By.XPATH, LogInPage.INPUT_PASSWORD).send_keys(password)

    # Входим в ЛК
    driver.find_element(By.XPATH, LogInPage.LOG_IN_BUTTON).click()

