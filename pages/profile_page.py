from locators.account_locators import ProfileLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def open_order_history(self):
        self.click(ProfileLocators.ORDER_HISTORY_LINK)

    def logout(self):
        self.click(ProfileLocators.LOGOUT_BUTTON)
        self.wait_until_url_contains("/login")

    def wait_for_profile(self):
        self.find(ProfileLocators.PROFILE_LINK)
