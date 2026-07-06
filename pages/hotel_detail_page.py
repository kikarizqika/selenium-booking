# pages/hotel_detail_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HotelDetailPage(BasePage):
    ROOM_CARD = (By.CLASS_NAME, "room-option-card")
    CONTINUE_BTN = (By.ID, "continue-btn")

    def select_room(self, room_type):
        locator = (By.XPATH, f"//label[contains(., '{room_type}')]/input")
        self.click(locator)
        self.click(self.CONTINUE_BTN)
