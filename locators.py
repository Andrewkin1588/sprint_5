class LogInMainPageLocators:
    PERSONAL_ACCOUNT_LINK = "//a[@href='/account']"  # Ссылка "Личный кабинет"
    LOG_IN_BUTTON = "//div[@class='BurgerConstructor_basket__container__2fUl3 mt-10']/button"  # Кнопка "Войти в аккаунт"


class ConstructorMainPage:
    CONSTRUCTOR_TAB = "//div[contains(@class,'tab_tab__1SPyG')]"  # Разделы конструктора


class PageRegistration:
    INPUT_NAME_EMAIL_PASSWORD = "//input[contains(@class,'input__textfield')]"  # Поля Имя, Email и Пароль на старнице Регистрации
    REGISTRATION_BUTTON = "//form[contains(@class,'Auth_form__3qKeq mb-20')]/button"  # Кнопка "Зарегестрироваться"
    INVALID_PASSWORD_ERROR = "//p[contains(@class,'input__error')]"


class LogInPage:
    INPUT_EMAIL = "//input[@type='text']"  # Поле для ввода Email
    INPUT_PASSWORD = "//input[@type='password']"  # Поле для ввода пароля
    LOG_IN_BUTTON = "//form[contains(@class,'Auth_form__3qKeq mb-20')]/button"  # Кнопка "Войти"
    REGISTRATION_LINK = "//a[@href='/register']" # Ссылка "Зарегистрироваться"
    FORGOT_PASSWORD_LINK = "//a[@href='/forgot-password']" # Ссылка "Зарегистрироваться"


class ForgotPasswordPage:
    INPUT_EMAIL = "//input[@type='text']"  # Поле для ввода Email
    RECOVER_BUTTON = "//form[contains(@class,'Auth_form__3qKeq mb-20')]/button"  # Кнопка "Восстановить"
