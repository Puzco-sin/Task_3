from locators.main_locators import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def open(self, base_url: str):
        return super().open(base_url)

    def open_profile(self):
        self.click(MainLocators.PERSONAL_ACCOUNT)

    def open_constructor(self):
        self.click(MainLocators.CONSTRUCTOR)

    def open_feed(self):
        self.click(MainLocators.FEED)

    def open_ingredient_details(self):
        self.click(MainLocators.BUN)

    def is_ingredient_modal_visible(self) -> bool:
        return self.is_visible(MainLocators.MODAL_TITLE)

    def close_modal(self):
        elements = self.find_all(MainLocators.MODAL_CLOSE)
        for element in elements:
            if element.is_displayed():
                self.driver.execute_script("arguments[0].click();", element)
                break
        self.wait.until(
            lambda driver: not any(
                element.is_displayed()
                for element in driver.find_elements(*MainLocators.MODAL_TITLE)
            )
        )

    def add_bun_to_order(self):
        bun = self.find(MainLocators.BUN)
        target = self.find(MainLocators.CONSTRUCTOR_DROP_ZONE)
        script = """
const source = arguments[0];
const target = arguments[1];
const data = new DataTransfer();
source.dispatchEvent(new DragEvent('dragstart', {bubbles: true, cancelable: true, dataTransfer: data}));
target.dispatchEvent(new DragEvent('dragenter', {bubbles: true, cancelable: true, dataTransfer: data}));
target.dispatchEvent(new DragEvent('dragover', {bubbles: true, cancelable: true, dataTransfer: data}));
target.dispatchEvent(new DragEvent('drop', {bubbles: true, cancelable: true, dataTransfer: data}));
source.dispatchEvent(new DragEvent('dragend', {bubbles: true, cancelable: true, dataTransfer: data}));
"""
        self.driver.execute_script(script, bun, target)
        self.wait.until(lambda driver: self.get_bun_counter() == 2)

    def get_bun_counter(self) -> int:
        elements = self.driver.find_elements(*MainLocators.INGREDIENT_COUNTER)
        if not elements:
            return 0
        text = elements[0].text.strip()
        return int(text) if text.isdigit() else 0

    def create_order(self):
        self.click(MainLocators.ORDER_BUTTON)

    def get_order_number(self) -> str:
        def get_real_number(driver):
            elements = driver.find_elements(*MainLocators.ORDER_NUMBER)
            for element in elements:
                text = element.text.strip()
                if text.isdigit() and text != "9999":
                    return str(int(text))
            return False

        return self.wait.until(get_real_number)
