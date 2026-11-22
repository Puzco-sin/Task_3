import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.feature("Личный кабинет")
class TestAccount:
    @allure.title("Переход в личный кабинет")
    def test_open_personal_account(self, driver, base_url, account):
        email, password = account
        with allure.step("Открыть страницу входа"):
            LoginPage(driver).open(base_url)
        with allure.step("Войти в тестовый аккаунт"):
            LoginPage(driver).login(email, password)
        with allure.step("Нажать на Личный Кабинет"):
            MainPage(driver).open_profile()
        with allure.step("Дождаться загрузки профиля"):
            ProfilePage(driver).wait_for_profile()
        with allure.step("Проверить переход в личный кабинет"):
            assert "/account/profile" in driver.current_url

    @allure.title("Переход в историю заказов")
    def test_open_order_history(self, driver, base_url, account):
        email, password = account
        with allure.step("Открыть страницу входа"):
            login = LoginPage(driver)
            login.open(base_url)
        with allure.step("Войти в тестовый аккаунт"):
            login.login(email, password)
        with allure.step("Открыть личный кабинет"):
            MainPage(driver).open_profile()
        with allure.step("Перейти в Историю заказов"):
            ProfilePage(driver).open_order_history()
        with allure.step("Проверить адрес страницы истории"):
            assert "/account/order-history" in driver.current_url

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, base_url, account):
        email, password = account
        with allure.step("Открыть страницу входа"):
            login = LoginPage(driver)
            login.open(base_url)
        with allure.step("Войти в тестовый аккаунт"):
            login.login(email, password)
        with allure.step("Открыть личный кабинет"):
            MainPage(driver).open_profile()
        with allure.step("Дождаться загрузки профиля"):
            profile = ProfilePage(driver)
            profile.wait_for_profile()
        with allure.step("Нажать кнопку Выход"):
            profile.logout()
        with allure.step("Проверить переход на страницу входа"):
            assert "/login" in driver.current_url
