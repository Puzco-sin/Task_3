from locators.feed_locators import FeedLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    def open_order_details(self):
        self.click(FeedLocators.ORDER_CARD)

    def is_order_modal_visible(self) -> bool:
        if "/feed/" not in self.driver.current_url:
            return False
        for modal in self.driver.find_elements(*FeedLocators.ORDER_MODAL):
            if modal.is_displayed() and modal.text.strip():
                return True
        return False

    def close_order_modal(self):
        self.click(FeedLocators.ORDER_MODAL_CLOSE)

    def get_all_time_counter(self) -> int:
        return int(self.find(FeedLocators.ALL_TIME_COUNTER).text)

    def get_today_counter(self) -> int:
        return int(self.find(FeedLocators.TODAY_COUNTER).text)

    def wait_for_counter_to_increase(self, getter, previous: int) -> bool:
        def counter_changed(driver):
            del driver
            return getter(self) > previous

        return self.wait.until(counter_changed)

    def get_in_progress_numbers(self) -> list[str]:
        numbers = []
        for element in self.find_all(FeedLocators.IN_PROGRESS):
            text = element.text.strip()
            if text.isdigit():
                numbers.append(str(int(text)))
        return numbers

    def get_order_numbers(self) -> list[str]:
        cards = self.find_all(FeedLocators.ORDER_CARD)
        return [card.text for card in cards]
