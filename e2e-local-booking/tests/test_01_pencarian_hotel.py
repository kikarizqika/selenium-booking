# tests/test_01_pencarian_hotel.py
from pages.home_page import BookNowHomePage
from pages.search_results_page import SearchResultsPage


class TestPencarianHotel:
    def test_cari_hotel_valid(self, driver):  # TC-01
        home = BookNowHomePage(driver)
        home.search_hotels('Jakarta')
        results = SearchResultsPage(driver)
        assert results.get_hotel_count() > 0, 'Harus ada hasil hotel'

    def test_cari_hotel_lokasi_kosong(self, driver):  # TC-02
        home = BookNowHomePage(driver)
        home.search_hotels('')
        assert 'harus diisi' in home.get_error_message().lower()
