from selenium.webdriver.common.by import By
from conftest import CreateUser, authoriztaion
from locators import LogInPage, LogInMainPageLocators, PersonalAccount


class TestLogInToPersonalAccount:
    def test_log_in_to_personal_account(self, driver, helpers):
        user = CreateUser.generate_user()
        email, password = user.email, user.password
        CreateUser(user.name, user.email, user.password).user_registration(driver, helpers)  # Регистрируем пользователя
        url = 'https://stellarburgers.nomoreparties.site/'
        driver.get(url)  # Переходим на главную

        helpers.wait_until_visibility_of_element_located(driver, LogInMainPageLocators.LOG_IN_BUTTON)
        driver.find_element(By.XPATH, LogInMainPageLocators.LOG_IN_BUTTON).click()

        helpers.wait_until_visibility_of_element_located(driver, LogInPage.LOG_IN_BUTTON)
        authoriztaion(driver, email, password)

        helpers.wait_until_visibility_of_element_located(driver, LogInMainPageLocators.PERSONAL_ACCOUNT_LINK)
        driver.find_element(By.XPATH, LogInMainPageLocators.PERSONAL_ACCOUNT_LINK).click()

        helpers.wait_until_visibility_of_element_located(driver, PersonalAccount.PROFILE_LINK)

        assert helpers.get_text_from_element(driver, PersonalAccount.PROFILE_LINK) == 'Профиль'

        driver.quit()