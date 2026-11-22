from selenium.webdriver.common.by import By


class MainLocators:
    PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет")
    CONSTRUCTOR = (By.LINK_TEXT, "Конструктор")
    FEED = (By.LINK_TEXT, "Лента Заказов")

    INGREDIENT = (By.XPATH, "//p[contains(@class, 'text') and contains(@class, 'text_type_main-default')]")
    MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")

    BUN = (By.XPATH, "//a[@draggable='true'][.//p[text()='Флюоресцентная булка R2-D3']]")
    SAUCE = (By.XPATH, "//p[text()='Соус Spicy-X']")
    CONSTRUCTOR_DROP_ZONE = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    INGREDIENT_COUNTER = (By.XPATH, "//a[.//p[text()='Флюоресцентная булка R2-D3']]//p[contains(@class, 'counter_counter__num')]")

    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__content')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
