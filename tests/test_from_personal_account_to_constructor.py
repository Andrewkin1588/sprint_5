from selenium.webdriver.common.by import By
from helpers import CreateUser, authoriztaion
from locators import LogInPage, LogInMainPageLocators, PersonalAccount, Constructor
from src import constants


class TestToConstructorFromPersonalAccount:
    def test_to_constructor_from_personal_account(self, driver, helpers):
        user = CreateUser.generate_user()
        email, password = user.email, user.password
        CreateUser(user.name, user.email, user.password).user_registration(driver, helpers)  # Регистрируем пользователя
        driver.get(constants.BASE_URL)  # Переходим на главную

        helpers.wait_until_visibility_of_element_located(driver, LogInMainPageLocators.LOG_IN_BUTTON)
        driver.find_element(By.XPATH, LogInMainPageLocators.LOG_IN_BUTTON).click()

        helpers.wait_until_visibility_of_element_located(driver, LogInPage.LOG_IN_BUTTON)
        authoriztaion(driver, email, password)

        helpers.wait_until_visibility_of_element_located(driver, LogInMainPageLocators.PERSONAL_ACCOUNT_LINK)
        driver.find_element(By.XPATH, LogInMainPageLocators.PERSONAL_ACCOUNT_LINK).click()

        helpers.wait_until_visibility_of_element_located(driver, PersonalAccount.PROFILE_LINK)
        driver.find_element(By.XPATH, Constructor.TO_CONSTRUCTOR_TITLE).click()

        helpers.wait_until_visibility_of_element_located(driver, Constructor.CONSTRUCTOR_TAB)
        driver.find_element(By.XPATH, LogInMainPageLocators.PERSONAL_ACCOUNT_LINK).click()

        driver.find_element(By.XPATH, Constructor.TO_CONSTRUCTOR_LOGO).click()
