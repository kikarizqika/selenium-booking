# pages/confirmation_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ConfirmationPage(BasePage):
    BOOKING_REF = (By.CLASS_NAME, "booking-reference-number")
    HISTORY_MENU = (By.ID, "history-menu-link")
    LOGIN_BTN = (By.ID, "login-btn")
    HISTORY_ITEM = (By.CLASS_NAME, "history-item-card")

    def get_booking_reference(self):
        return self.driver.find_element(*self.BOOKING_REF).text

    def open_order_history(self):
        self.click(self.HISTORY_MENU)
        # Aplikasi demo memerlukan login sederhana sebelum riwayat tampil
        self.click(self.LOGIN_BTN)
