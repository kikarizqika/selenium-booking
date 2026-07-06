# tests/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "http://127.0.0.1:5000"


@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    # Hapus baris di bawah ini jika ingin melihat browser berjalan (tidak headless)
    # chrome_options.add_argument("--headless=new")

    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=chrome_options)
    yield drv
    drv.quit()
