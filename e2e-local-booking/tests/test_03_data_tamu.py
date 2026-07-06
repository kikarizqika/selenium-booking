# tests/test_03_data_tamu.py
from pages.booking_form_page import BookingFormPage


class TestDataTamu:
    def test_isi_data_tamu_valid(self, driver):  # TC-05
        form = BookingFormPage(driver)
        form.fill_guest_data('Budi Santoso', 'budi@email.com')
        assert 'payment' in driver.current_url

    def test_isi_data_tamu_email_tidak_valid(self, driver):  # TC-06
        driver.get("http://127.0.0.1:5000/booking-form")
        form = BookingFormPage(driver)
        form.fill_guest_data('Test User', 'notanemail')
        assert form.is_visible(form.EMAIL_ERROR)
