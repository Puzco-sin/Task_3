import allure

from pages.password_page import PasswordPage


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля")
    def test_go_to_password_recovery(self, driver, base_url):
        with allure.step("Открыть страницу восстановления пароля"):
            page = PasswordPage(driver)
            page.open_recovery(base_url)
        with allure.step("Проверить адрес страницы восстановления"):
            assert "forgot-password" in driver.current_url

    @allure.title("Ввод email и отправка формы восстановления")
    def test_restore_password_with_email(self, driver, base_url, account):
        email = account[0]
        with allure.step("Открыть страницу восстановления пароля"):
            page = PasswordPage(driver)
            page.open_recovery(base_url)
        with allure.step("Ввести email"):
            page.enter_email(email)
        with allure.step("Нажать кнопку Восстановить"):
            page.restore_password()
        with allure.step("Проверить переход на страницу восстановления"):
            assert "/forgot-password" in driver.current_url

    @allure.title("Кнопка показать пароль активирует поле")
    def test_show_password_activates_field(self, driver, base_url):
        with allure.step("Открыть страницу входа"):
            page = PasswordPage(driver)
            page.open_login_password(base_url)
        with allure.step("Ввести пароль"):
            page.enter_login_password("QaPassword123")
        with allure.step("Нажать кнопку показать пароль"):
            page.show_login_password()
        with allure.step("Проверить, что поле активировано"):
            assert page.is_password_field_active()
