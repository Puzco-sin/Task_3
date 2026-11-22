from locators.account_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def open(self, base_url: str):
        return super().open(base_url + "/login")

    def login(self, email: str, password: str):
        self.enter_text(LoginLocators.EMAIL_INPUT, email)
        self.enter_text(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)
        self.wait.until(lambda driver: "/login" not in driver.current_url)
