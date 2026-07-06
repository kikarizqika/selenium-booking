# pages/payment_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PaymentPage(BasePage):
    CREDIT_CARD_OPTION = (By.ID, "credit-card-option")
    CARD_NUMBER_INPUT = (By.ID, "card-number")
    CVV_INPUT = (By.ID, "card-cvv")
    PAY_BTN = (By.ID, "pay-btn")
    ERROR_MSG = (By.CLASS_NAME, "payment-error-message")

    def select_credit_card(self):
        self.click(self.CREDIT_CARD_OPTION)

    def pay_with_card(self, card_number, cvv):
        self.type(self.CARD_NUMBER_INPUT, card_number)
        self.type(self.CVV_INPUT, cvv)
        self.click(self.PAY_BTN)
