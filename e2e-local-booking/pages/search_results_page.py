# pages/search_results_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    HOTEL_CARD = (By.CLASS_NAME, "hotel-card")

    def get_hotel_count(self):
        return len(self.driver.find_elements(*self.HOTEL_CARD))

    def select_first_hotel(self):
        self.click(self.HOTEL_CARD)
