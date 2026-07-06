# tests/test_02_pemilihan_hotel.py
from pages.home_page import BookNowHomePage
from pages.search_results_page import SearchResultsPage
from pages.hotel_detail_page import HotelDetailPage


class TestPemilihanHotel:
    def test_pilih_hotel_dari_hasil_pencarian(self, driver):  # TC-03
        home = BookNowHomePage(driver)
        home.search_hotels('Jakarta')
        results = SearchResultsPage(driver)
        results.select_first_hotel()
        detail = HotelDetailPage(driver)
        assert detail.is_visible(detail.ROOM_CARD)

    def test_pilih_tipe_kamar_dan_lanjut(self, driver):  # TC-04
        detail = HotelDetailPage(driver)
        detail.select_room('Deluxe')
        assert 'booking-form' in driver.current_url
