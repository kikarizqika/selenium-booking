# pages/home_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

BASE_URL = "http://127.0.0.1:5000"


class BookNowHomePage(BasePage):
    URL = BASE_URL
    LOCATION_INPUT = (By.ID, "hotel-search-box")
    SEARCH_BTN = (By.ID, "search-btn")
    ERROR_MSG = (By.CLASS_NAME, "search-error-message")

    def search_hotels(self, location, checkin="2026-07-15", checkout="2026-07-17"):
        self.open(self.URL)
        if location:
            self.type(self.LOCATION_INPUT, location)
        self.click(self.SEARCH_BTN)

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MSG).text
