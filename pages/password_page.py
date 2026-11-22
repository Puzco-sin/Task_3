from locators.account_locators import PasswordLocators
from pages.base_page import BasePage


class PasswordPage(BasePage):
    def open_recovery(self, base_url: str):
        self.open(base_url + "/login")
        self.click(PasswordLocators.RESTORE_PASSWORD_LINK)

    def enter_email(self, email: str):
        self.enter_text(PasswordLocators.EMAIL_INPUT, email)

    def restore_password(self):
        self.click(PasswordLocators.RESTORE_BUTTON)

    def show_password(self):
        self.click(PasswordLocators.SHOW_PASSWORD_BUTTON)

    def open_login_password(self, base_url: str):
        self.open(base_url + "/login")

    def enter_login_password(self, password: str):
        self.enter_text(PasswordLocators.LOGIN_PASSWORD_INPUT, password)

    def show_login_password(self):
        self.click(PasswordLocators.LOGIN_SHOW_PASSWORD_BUTTON)

    def is_password_field_active(self) -> bool:
        element = self.find(PasswordLocators.LOGIN_PASSWORD_INPUT)
        parent_class = element.find_element("xpath", "..").get_attribute("class") or ""
        return "input_status_active" in parent_class and element.get_attribute("type") == "text"
