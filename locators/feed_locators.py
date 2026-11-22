from selenium.webdriver.common.by import By


class FeedLocators:
    ORDER_CARD = (By.CSS_SELECTOR, "li.OrderHistory_listItem__2x95r")
    ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    ORDER_MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    ALL_TIME_COUNTER = (By.XPATH, "//p[contains(text(),'Выполнено за все')]/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p")
    IN_PROGRESS = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul/li")
