# pages/booking_form_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BookingFormPage(BasePage):
    NAME_INPUT = (By.ID, "guest-name")
    EMAIL_INPUT = (By.ID, "guest-email")
    NEXT_BTN = (By.ID, "next-btn")
    EMAIL_ERROR = (By.CLASS_NAME, "email-error-text")

    def fill_guest_data(self, name, email):
        self.type(self.NAME_INPUT, name)
        self.type(self.EMAIL_INPUT, email)
        self.click(self.NEXT_BTN)
