from selenium.webdriver.common.by import By
from conftest import CreateUser, authoriztaion
from locators import PageRegistration, LogInPage, LogInMainPageLocators, GetOrder



class TestLogIn:
    # Вход по кнопке "Войти в аккаунт"
    def test_log_in_from_personal_account_button(self, driver, helpers):
        user = CreateUser.generate_user()
        email, password = user.email, user.password
        CreateUser(user.name, user.email, user.password).user_registration(driver, helpers) # Регистрируем пользователя
        url = 'https://stellarburgers.nomoreparties.site/'
        driver.get(url) # Переходим на главную

        helpers.wait_until_visibility_of_element_located(driver, LogInMainPageLocators.LOG_IN_BUTTON)

        driver.find_element(By.XPATH, LogInMainPageLocators.LOG_IN_BUTTON).click()

        helpers.wait_until_visibility_of_element_located(driver, LogInPage.INPUT_EMAIL)

        authoriztaion(driver, email, password)

        # Ожидаем загрузки страницы
        helpers.wait_until_visibility_of_element_located(driver, GetOrder.ORDER_BUTTON)

        assert helpers.get_text_from_element(driver, GetOrder.ORDER_BUTTON) == 'Оформить заказ'

        driver.quit()

    # Вход по линку "Личный кабинет"
    def test_log_in_from_personal_account_link(self, driver, helpers):
        user = CreateUser.generate_user()
        email, password = user.email, user.password
        CreateUser(user.name, user.email, user.password).user_registration(driver, helpers)

        url = 'https://stellarburgers.nomoreparties.site/'
        driver.get(url)  # Переходим на главную

        helpers.wait_until_visibility_of_element_located(driver, LogInMainPageLocators.PERSONAL_ACCOUNT_LINK)

        driver.find_element(By.XPATH, LogInMainPageLocators.PERSONAL_ACCOUNT_LINK).click()

        helpers.wait_until_visibility_of_element_located(driver, LogInPage.INPUT_EMAIL)

        authoriztaion(driver, email, password)

        # Ожидаем загрузки страницы
        helpers.wait_until_visibility_of_element_located(driver, GetOrder.ORDER_BUTTON)

        assert helpers.get_text_from_element(driver, GetOrder.ORDER_BUTTON) == 'Оформить заказ'
        driver.quit()

    # Вход через страницу регистрации
    def test_log_in_from_registration_page(self, driver, helpers):
        user = CreateUser.generate_user()
        email, password = user.email, user.password
        CreateUser(user.name, user.email, user.password).user_registration(driver, helpers)

        url = 'https://stellarburgers.nomoreparties.site/'
        driver.get(url)  # Переходим на главную

        helpers.wait_until_visibility_of_element_located(driver, LogInMainPageLocators.LOG_IN_BUTTON)

        driver.find_element(By.XPATH, LogInMainPageLocators.LOG_IN_BUTTON).click()

        helpers.wait_until_visibility_of_element_located(driver, LogInPage.REGISTRATION_LINK)

        driver.find_element(By.XPATH, LogInPage.REGISTRATION_LINK).click()

        helpers.wait_until_visibility_of_element_located(driver, PageRegistration.LOG_IN_LINK)

        driver.find_element(By.XPATH, PageRegistration.LOG_IN_LINK).click()

        authoriztaion(driver, email, password)

        helpers.wait_until_visibility_of_element_located(driver, GetOrder.ORDER_BUTTON)

        assert helpers.get_text_from_element(driver, GetOrder.ORDER_BUTTON) == 'Оформить заказ'
        driver.quit()

    # Вход через страницу забыли пароль
    def test_log_in_from_forgot_password_page(self, driver, helpers):
        user = CreateUser.generate_user()
        email, password = user.email, user.password
        CreateUser(user.name, user.email, user.password).user_registration(driver, helpers)

        url = 'https://stellarburgers.nomoreparties.site/'
        driver.get(url)  # Переходим на главную

        helpers.wait_until_visibility_of_element_located(driver, LogInMainPageLocators.LOG_IN_BUTTON)

        driver.find_element(By.XPATH, LogInMainPageLocators.LOG_IN_BUTTON).click()

        helpers.wait_until_visibility_of_element_located(driver, LogInPage.FORGOT_PASSWORD_LINK)

        driver.find_element(By.XPATH, LogInPage.FORGOT_PASSWORD_LINK).click()

        helpers.wait_until_visibility_of_element_located(driver, PageRegistration.LOG_IN_LINK)

        driver.find_element(By.XPATH, PageRegistration.LOG_IN_LINK).click()

        authoriztaion(driver, email, password)

        helpers.wait_until_visibility_of_element_located(driver, GetOrder.ORDER_BUTTON)

        assert helpers.get_text_from_element(driver, GetOrder.ORDER_BUTTON) == 'Оформить заказ'

        driver.quit()