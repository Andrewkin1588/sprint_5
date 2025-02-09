class LogInMainPageLocators:
    PERSONAL_ACCOUNT_LINK = "//a[@href='/account']"  # Ссылка "Личный кабинет"
    LOG_IN_BUTTON = "//div[@class='BurgerConstructor_basket__container__2fUl3 mt-10']/button"  # Кнопка "Войти в аккаунт"


class Constructor:
    CONSTRUCTOR_TAB = "//div[contains(@class,'tab_tab_type_current__2BEPc')]" # Переключение
    CONSTRUCTOR_TAB_TEXT = "//span[contains(@class,'text_type_main-default')]"  # Раздел конструктора
    TO_CONSTRUCTOR_LOGO = "//div[@class='AppHeader_header__logo__2D0X2']//a[@href='/']" # Лого
    TO_CONSTRUCTOR_TITLE = "//ul[@class='AppHeader_header__list__3oKJj']//a[@href='/']" # Раздел  конструктор


class PageRegistration:
    INPUT_NAME_EMAIL_PASSWORD = "//input[contains(@class,'input__textfield')]"  # Поля Имя, Email и Пароль на старнице Регистрации
    REGISTRATION_BUTTON = "//form[contains(@class,'Auth_form__3qKeq mb-20')]/button"  # Кнопка "Зарегестрироваться"
    INVALID_PASSWORD_ERROR = "//p[contains(@class,'input__error')]"  # Ошибка некорректного пароля
    LOG_IN_LINK = "//a[@href='/login']"  # Ссылка на вход


class LogInPage:
    INPUT_EMAIL = "//input[@type='text']"  # Поле для ввода Email
    INPUT_PASSWORD = "//input[@type='password']"  # Поле для ввода пароля
    LOG_IN_BUTTON = "//form[contains(@class,'Auth_form__3qKeq mb-20')]/button"  # Кнопка "Войти"
    REGISTRATION_LINK = "//a[@href='/register']"  # Ссылка "Зарегистрироваться"
    FORGOT_PASSWORD_LINK = "//a[@href='/forgot-password']"  # Ссылка "Зарегистрироваться"


class ForgotPasswordPage:
    INPUT_EMAIL = "//input[@type='text']"  # Поле для ввода Email
    RECOVER_BUTTON = "//form[contains(@class,'Auth_form__3qKeq mb-20')]/button"  # Кнопка "Восстановить"


class GetOrder:
    ORDER_BUTTON = "//div[contains(@class,'BurgerConstructor_basket__container__2fUl3')]/button"  # Кнопка "Оформить заказ"


class PersonalAccount:
    PROFILE_LINK = "//a[@href='/account/profile']"  # раздел "Профиль" в личном кабинете
    LOG_OUT_BUTTON = "//li[@class='Account_listItem__35dAP']/button" # Кнопка "Выход"
