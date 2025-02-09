from selenium.webdriver.common.by import By
from helpers import GenerateTestData, registration
from locators import PageRegistration, LogInPage


generator = GenerateTestData()


class TestRegistration:
    def test_registration_positive(self, driver, helpers):
        registration(driver, helpers)
        # Заполняем поля для регистрации
        fields_input = driver.find_elements(By.XPATH, PageRegistration.INPUT_NAME_EMAIL_PASSWORD)
        fields_input[0].send_keys(generator.generate_name())
        fields_input[1].send_keys(generator.generate_email())
        fields_input[2].send_keys(generator.generate_password())

        # Нажимаем кнопку "Зарегистрироваться"
        driver.find_element(By.XPATH, PageRegistration.REGISTRATION_BUTTON).click()

        # Ожидаем появления кнопки "Войти" после успешной регистрации
        helpers.wait_until_visibility_of_element_located(driver, LogInPage.LOG_IN_BUTTON)

    def test_registration_negative(self, driver, helpers):
        registration(driver, helpers)
        # Заполняем поля для регистрации
        fields_input = driver.find_elements(By.XPATH, PageRegistration.INPUT_NAME_EMAIL_PASSWORD)
        fields_input[0].send_keys(generator.generate_name())
        fields_input[1].send_keys(generator.generate_email())
        fields_input[2].send_keys(generator.generate_password_negative())

        # Нажимаем кнопку "Зарегистрироваться"
        driver.find_element(By.XPATH, PageRegistration.REGISTRATION_BUTTON).click()

        # Ожидаем появления ошибки "Некорректный пароль" т.к. кол-во символов меньше чем должно быть
        helpers.wait_until_visibility_of_element_located(driver, PageRegistration.INVALID_PASSWORD_ERROR)

        # Проверяем текст сообщения о некорректном пароле
        invalid_password_text = driver.find_element(By.XPATH, PageRegistration.INVALID_PASSWORD_ERROR).text
        assert invalid_password_text == 'Некорректный пароль'
