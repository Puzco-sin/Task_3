from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, url: str):
        self.driver.get(url)
        return self

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(lambda driver: driver.find_elements(*locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def enter_text(self, locator, text: str):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator) -> bool:
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def wait_until_url_contains(self, text: str):
        self.wait.until(EC.url_contains(text))
