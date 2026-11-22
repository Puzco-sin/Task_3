import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature("Основной функционал")
class TestMainFunctionality:
    @allure.title("Переход по клику на Конструктор")
    def test_open_constructor(self, driver, base_url):
        with allure.step("Открыть главную страницу"):
            page = MainPage(driver)
            page.open(base_url)
        with allure.step("Перейти в Ленту заказов"):
            page.open_feed()
        with allure.step("Нажать на Конструктор"):
            page.open_constructor()
        with allure.step("Проверить адрес главной страницы"):
            assert driver.current_url.rstrip("/") == base_url.rstrip("/")

    @allure.title("Переход по клику на Лента заказов")
    def test_open_feed(self, driver, base_url):
        with allure.step("Открыть главную страницу"):
            page = MainPage(driver)
            page.open(base_url)
        with allure.step("Нажать на Лента заказов"):
            page.open_feed()
        with allure.step("Проверить переход в Ленту заказов"):
            assert "/feed" in driver.current_url

    @allure.title("Открытие всплывающего окна с деталями ингредиента")
    def test_open_ingredient_details(self, driver, base_url):
        with allure.step("Открыть главную страницу"):
            page = MainPage(driver)
            page.open(base_url)
        with allure.step("Нажать на ингредиент"):
            page.open_ingredient_details()
        with allure.step("Проверить отображение окна деталей"):
            assert page.is_ingredient_modal_visible()

    @allure.title("Закрытие всплывающего окна ингредиента")
    def test_close_ingredient_details(self, driver, base_url):
        with allure.step("Открыть главную страницу"):
            page = MainPage(driver)
            page.open(base_url)
        with allure.step("Открыть окно деталей ингредиента"):
            page.open_ingredient_details()
        with allure.step("Закрыть окно по крестику"):
            page.close_modal()
        with allure.step("Проверить закрытие окна"):
            assert not page.is_ingredient_modal_visible()

    @allure.title("Увеличение счетчика добавленного ингредиента")
    def test_ingredient_counter_increases(self, driver, base_url):
        with allure.step("Открыть главную страницу"):
            page = MainPage(driver)
            page.open(base_url)
        with allure.step("Проверить начальное значение каунтера"):
            assert page.get_bun_counter() == 0
        with allure.step("Добавить булку в заказ"):
            page.add_bun_to_order()
        with allure.step("Проверить увеличение каунтера до двух"):
            assert page.get_bun_counter() == 2

    @allure.title("Залогиненный пользователь оформляет заказ")
    def test_authenticated_user_creates_order(self, driver, base_url, account):
        email, password = account
        with allure.step("Открыть страницу входа"):
            login = LoginPage(driver)
            login.open(base_url)
        with allure.step("Войти в тестовый аккаунт"):
            login.login(email, password)
        with allure.step("Открыть главную страницу"):
            page = MainPage(driver)
            page.open(base_url)
        with allure.step("Добавить булку в заказ"):
            page.add_bun_to_order()
        with allure.step("Оформить заказ"):
            page.create_order()
        with allure.step("Проверить получение номера заказа"):
            assert page.get_order_number().isdigit()
