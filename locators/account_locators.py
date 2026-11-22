from selenium.webdriver.common.by import By


class PasswordLocators:
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    RESET_PASSWORD_INPUT = (By.XPATH, "//label[text()='Введите новый пароль']/following-sibling::input")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_SHOW_PASSWORD_BUTTON = (By.XPATH, "//label[text()='Пароль']/following-sibling::input/../div[contains(@class, 'input__icon')]")


class LoginLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")


class ProfileLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
