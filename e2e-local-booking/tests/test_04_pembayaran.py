# tests/test_04_pembayaran.py
from pages.payment_page import PaymentPage


class TestPembayaran:
    def test_pilih_metode_kartu_kredit(self, driver):  # TC-07
        driver.get("http://127.0.0.1:5000/payment")
        payment = PaymentPage(driver)
        payment.select_credit_card()
        assert payment.is_visible(payment.CARD_NUMBER_INPUT)

    def test_bayar_dengan_kartu_tidak_valid(self, driver):  # TC-09
        driver.get("http://127.0.0.1:5000/payment")
        payment = PaymentPage(driver)
        payment.select_credit_card()
        payment.pay_with_card('0000000000000000', '000')
        assert 'gagal' in payment.driver.find_element(
            *payment.ERROR_MSG).text.lower()

    def test_bayar_dengan_kartu_valid(self, driver):  # TC-08
        driver.get("http://127.0.0.1:5000/payment")
        payment = PaymentPage(driver)
        payment.select_credit_card()
        payment.pay_with_card('4111111111111111', '123')
        assert 'confirmation' in driver.current_url
