import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import Helpers, GenerateTestData
from locators import LogInMainPageLocators, PageRegistration, LogInPage

driver = webdriver.Chrome()
helper = Helpers()
generator = GenerateTestData()


def test_registration_positive():
    # Переходим на главную страницу
    url = 'https://stellarburgers.nomoreparties.site/'
    driver.get(url)

    # Ожидаем появлния кнопки "Войти в аккаунт"
    helper.wait_until_visibility_of_element_located(driver, LogInMainPageLocators.LOG_IN_BUTTON)

    # Нажимаем на кнопку "Войти в аккаунт"
    driver.find_element(By.XPATH, LogInMainPageLocators.LOG_IN_BUTTON).click()

    # Ожидаем появления ссылки "Зарегистрироваться"
    helper.wait_until_visibility_of_element_located(driver, LogInPage.REGISTRATION_LINK)

    # Нажимаем на линк "Зарегистрироваться"
    driver.find_element(By.XPATH, LogInPage.REGISTRATION_LINK).click()

    # Ожидаем появления полей для ввода
    helper.wait_until_visibility_of_element_located(driver, PageRegistration.INPUT_NAME_EMAIL_PASSWORD)

    # Заполняем поля для регистрации
    fields_input = driver.find_elements(By.XPATH, PageRegistration.INPUT_NAME_EMAIL_PASSWORD)
    fields_input[0].send_keys(generator.generate_name())
    fields_input[1].send_keys(generator.generate_email())
    fields_input[2].send_keys(generator.generate_password())

    # Нажимаем кнопку "Зарегистрироваться"
    driver.find_element(By.XPATH, PageRegistration.REGISTRATION_BUTTON).click()

    # Ожидаем появления кнопки "Войти" после успешной регистрации
    helper.wait_until_visibility_of_element_located(driver, LogInPage.LOG_IN_BUTTON)

    # Закрываем браузер
    driver.quit()

def test_registration_negative():
    # Переходим на главную страницу
    url = 'https://stellarburgers.nomoreparties.site/'
    driver.get(url)

    # Ожидаем появлния кнопки "Войти в аккаунт"
    helper.wait_until_visibility_of_element_located(driver, LogInMainPageLocators.LOG_IN_BUTTON)

    # Нажимаем на кнопку "Войти в аккаунт"
    driver.find_element(By.XPATH, LogInMainPageLocators.LOG_IN_BUTTON).click()

    # Ожидаем появления ссылки "Зарегистрироваться"
    helper.wait_until_visibility_of_element_located(driver, LogInPage.REGISTRATION_LINK)

    # Нажимаем на линк "Зарегистрироваться"
    driver.find_element(By.XPATH, LogInPage.REGISTRATION_LINK).click()

    # Ожидаем появления полей для ввода
    helper.wait_until_visibility_of_element_located(driver, PageRegistration.INPUT_NAME_EMAIL_PASSWORD)

    # Заполняем поля для регистрации
    fields_input = driver.find_elements(By.XPATH, PageRegistration.INPUT_NAME_EMAIL_PASSWORD)
    fields_input[0].send_keys(generator.generate_name())
    fields_input[1].send_keys(generator.generate_email())
    fields_input[2].send_keys(generator.generate_password_negative())

    # Нажимаем кнопку "Зарегистрироваться"
    driver.find_element(By.XPATH, PageRegistration.REGISTRATION_BUTTON).click()

    # Ожидаем появления ошибки "Некорректный пароль" т.к. кол-во символов меньше чем должно быть
    helper.wait_until_visibility_of_element_located(driver, PageRegistration.INVALID_PASSWORD_ERROR)

    # Проверяем текст сообщения о некорректном пароле
    invalid_password_text = driver.find_element(By.XPATH, PageRegistration.INVALID_PASSWORD_ERROR).text
    assert invalid_password_text == 'Некорректный пароль'

    # Закрываем браузер
    driver.quit()
