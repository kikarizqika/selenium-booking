# BookNow Demo — E2E Testing dengan Selenium & Allure

Proyek ini berisi dua bagian:
1. **`app.py`** — sistem reservasi hotel lokal (mock booking system) yang berjalan
   di komputer sendiri, sengaja dibuat sederhana agar bisa diuji end-to-end secara
   nyata (bukan simulasi).
2. **`pages/` & `tests/`** — Page Object Model + test Selenium yang menguji sistem
   tersebut, dilengkapi pelaporan Allure.

Kenapa tidak menguji Traveloka asli? Traveloka adalah aplikasi produksi dengan
struktur halaman yang berubah-ubah, proteksi anti-bot, dan captcha, sehingga
selector pada laporan lama (`#hotel-search-box`, dll.) tidak pernah benar-benar
cocok dengan halaman aslinya — itulah sebabnya screenshot sebelumnya tidak bisa
dihasilkan secara jujur. Sistem lokal ini meniru alur bisnis yang sama persis
(cari hotel → pilih kamar → isi data tamu → bayar → konfirmasi → riwayat)
sehingga metodologi pengujian yang dipelajari tetap sama, tapi hasilnya bisa
dijalankan dan di-screenshot sendiri.

## 1. Instalasi

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Pastikan Google Chrome sudah terpasang di komputer.

Install Allure Commandline (untuk melihat laporan):
```bash
# Mac
brew install allure
# Windows (pakai scoop)
scoop install allure
# Linux
sudo apt install allure
```
Jika tidak ada package manager tersebut, unduh manual dari:
https://github.com/allure-framework/allure2/releases lalu tambahkan folder
`bin` ke PATH.

## 2. Jalankan sistem demo

Buka terminal pertama:
```bash
python app.py
```
Biarkan tetap berjalan (jangan ditutup), lalu cek di browser: http://127.0.0.1:5000

## 3. Jalankan pengujian Selenium + Allure

Buka terminal kedua (biarkan terminal pertama tetap jalan):
```bash
pytest tests/ --alluredir=reports/allure-results -v
```
Chrome akan terbuka otomatis dan menjalankan setiap skenario — inilah yang bisa
Anda rekam/screenshot sebagai bukti proses berjalan.

## 4. Lihat & screenshot laporan Allure

```bash
allure serve reports/allure-results
```
Browser akan terbuka menampilkan dashboard Allure. Ambil screenshot pada:
- Halaman **Overview** (ringkasan pass/fail & severity) → untuk bagian 6.3 laporan
- Halaman **Suites**, klik salah satu test (disarankan `test_alur_penuh_e2e`)
  untuk melihat rincian `allure.step` beserta lampiran screenshot → bagian 6.4
- Output terminal saat `pytest` berjalan → bagian 6.5

## 5. Isi ulang bagian hasil di laporan Word

Setelah pengujian selesai, buka laporan `.docx` yang sudah diperbaiki, lalu:
- Ganti seluruh `[ISI]` di tabel 6.1 dan 6.2 dengan status/durasi asli dari
  Allure/terminal.
- Tempel 3 screenshot asli di bagian 6.3, 6.4, 6.5 (hapus kotak keterangan).

## Struktur Folder

```
e2e-local-booking/
├── app.py                     <- Aplikasi Flask (sistem yang diuji)
├── templates/                 <- Halaman HTML aplikasi
├── static/style.css
├── pages/                     <- Page Object Model
├── tests/                     <- Test Selenium + Allure
├── data/booking_data.csv      <- Data uji (Data-Driven Testing)
├── reports/                   <- Output Allure (dibuat otomatis)
├── requirements.txt
└── pytest.ini
```
