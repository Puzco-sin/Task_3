import allure

from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature("Лента заказов")
class TestFeed:
    @allure.title("Открытие деталей заказа")
    def test_open_order_details(self, driver, base_url):
        with allure.step("Открыть главную страницу"):
            page = MainPage(driver)
            page.open(base_url)
        with allure.step("Перейти в Ленту заказов"):
            page.open_feed()
        with allure.step("Нажать на заказ"):
            feed = FeedPage(driver)
            feed.open_order_details()
        with allure.step("Проверить открытие окна деталей заказа"):
            assert feed.is_order_modal_visible()

    @allure.title("Заказ пользователя отображается в ленте")
    def test_user_order_is_in_feed(self, driver, base_url, account):
        email, password = account
        with allure.step("Открыть страницу входа"):
            login = LoginPage(driver)
            login.open(base_url)
        with allure.step("Войти в тестовый аккаунт"):
            login.login(email, password)
        with allure.step("Открыть главную страницу"):
            main = MainPage(driver)
            main.open(base_url)
        with allure.step("Добавить булку в заказ"):
            main.add_bun_to_order()
        with allure.step("Оформить заказ"):
            main.create_order()
            order_number = main.get_order_number()
        with allure.step("Перейти в Ленту заказов"):
            main.open_feed()
        with allure.step("Проверить наличие номера заказа в ленте"):
            feed = FeedPage(driver)
            assert any(order_number in text for text in feed.get_order_numbers())

    @allure.title("Счетчик выполнено за все время увеличивается")
    def test_all_time_counter_increases(self, driver, base_url, account):
        email, password = account
        with allure.step("Открыть страницу входа"):
            login = LoginPage(driver)
            login.open(base_url)
        with allure.step("Войти в тестовый аккаунт"):
            login.login(email, password)
        with allure.step("Открыть Ленту заказов"):
            main = MainPage(driver)
            main.open(base_url)
            main.open_feed()
            feed = FeedPage(driver)
        with allure.step("Запомнить счётчик Выполнено за всё время"):
            before = feed.get_all_time_counter()
        with allure.step("Оформить новый заказ"):
            main.open(base_url)
            main.add_bun_to_order()
            main.create_order()
            main.get_order_number()
        with allure.step("Перейти в Ленту заказов"):
            main.open_feed()
        with allure.step("Проверить увеличение счётчика"):
            assert feed.wait_for_counter_to_increase(
                FeedPage.get_all_time_counter,
                before,
            )

    @allure.title("Счетчик выполнено за сегодня увеличивается")
    def test_today_counter_increases(self, driver, base_url, account):
        email, password = account
        with allure.step("Открыть страницу входа"):
            login = LoginPage(driver)
            login.open(base_url)
        with allure.step("Войти в тестовый аккаунт"):
            login.login(email, password)
        with allure.step("Открыть Ленту заказов"):
            main = MainPage(driver)
            main.open(base_url)
            main.open_feed()
            feed = FeedPage(driver)
        with allure.step("Запомнить счётчик Выполнено за сегодня"):
            before = feed.get_today_counter()
        with allure.step("Оформить новый заказ"):
            main.open(base_url)
            main.add_bun_to_order()
            main.create_order()
            main.get_order_number()
        with allure.step("Перейти в Ленту заказов"):
            main.open_feed()
        with allure.step("Проверить увеличение счётчика"):
            assert feed.wait_for_counter_to_increase(
                FeedPage.get_today_counter,
                before,
            )

    @allure.title("Номер нового заказа появляется в разделе В работе")
    def test_order_number_appears_in_progress(self, driver, base_url, account):
        email, password = account
        with allure.step("Открыть страницу входа"):
            login = LoginPage(driver)
            login.open(base_url)
        with allure.step("Войти в тестовый аккаунт"):
            login.login(email, password)
        with allure.step("Открыть главную страницу"):
            main = MainPage(driver)
            main.open(base_url)
        with allure.step("Добавить булку в заказ"):
            main.add_bun_to_order()
        with allure.step("Оформить заказ"):
            main.create_order()
            order_number = main.get_order_number()
        with allure.step("Перейти в Ленту заказов"):
            main.open_feed()
        with allure.step("Проверить номер заказа в разделе В работе"):
            feed = FeedPage(driver)
            assert order_number in feed.get_in_progress_numbers()
