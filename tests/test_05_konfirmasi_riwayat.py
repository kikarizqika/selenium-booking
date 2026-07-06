# tests/test_05_konfirmasi_riwayat.py
import allure
from pages.home_page import BookNowHomePage
from pages.search_results_page import SearchResultsPage
from pages.hotel_detail_page import HotelDetailPage
from pages.booking_form_page import BookingFormPage
from pages.payment_page import PaymentPage
from pages.confirmation_page import ConfirmationPage


class TestKonfirmasiRiwayat:
    def test_halaman_konfirmasi_tampil(self, driver):  # TC-10
        confirm = ConfirmationPage(driver)
        assert confirm.get_booking_reference() != ''

    def test_pesanan_tampil_di_riwayat(self, driver):  # TC-11
        confirm = ConfirmationPage(driver)
        confirm.open_order_history()
        assert confirm.is_visible(confirm.HISTORY_ITEM)

    @allure.feature('Hotel Booking')
    @allure.story('End-to-End Booking Flow')
    @allure.title('E2E: Pemesanan hotel lengkap di BookNow Demo')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_alur_penuh_e2e(self, driver):  # TC-12
        with allure.step('Cari hotel di Jakarta'):
            home = BookNowHomePage(driver)
            home.search_hotels('Jakarta')
        with allure.step('Pilih hotel & kamar'):
            SearchResultsPage(driver).select_first_hotel()
            HotelDetailPage(driver).select_room('Deluxe')
        with allure.step('Isi data tamu'):
            BookingFormPage(driver).fill_guest_data(
                'Budi Santoso', 'budi@email.com')
        with allure.step('Lakukan pembayaran'):
            payment = PaymentPage(driver)
            payment.select_credit_card()
            payment.pay_with_card('4111111111111111', '123')
        with allure.step('Verifikasi konfirmasi pemesanan'):
            confirm = ConfirmationPage(driver)
            allure.attach(
                driver.get_screenshot_as_png(),
                name='booking_confirmation',
                attachment_type=allure.attachment_type.PNG,
            )
            assert confirm.get_booking_reference() != ''
