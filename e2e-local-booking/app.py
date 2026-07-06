"""
BookNow Demo - Sistem Reservasi Hotel Lokal (untuk keperluan latihan E2E Testing)
----------------------------------------------------------------------------
Ini BUKAN Traveloka. Ini adalah aplikasi web sederhana yang dibuat sendiri
agar mahasiswa punya sistem booking online yang benar-benar bisa dijalankan
dan diuji end-to-end secara nyata (bukan simulasi/hasil rekaan), lengkap
dengan bukti screenshot asli dari Selenium + Allure.

Jalankan dengan:
    pip install -r requirements.txt
    python app.py
Lalu buka http://127.0.0.1:5000
"""
from flask import Flask, render_template, request, redirect, url_for, session
import uuid

app = Flask(__name__)
app.secret_key = "secret-key-for-demo-only"

HOTELS = [
    {"id": 1, "name": "Hotel Anggrek Jakarta", "location": "Jakarta",
     "rooms": ["Standard", "Deluxe", "Suite"]},
    {"id": 2, "name": "Hotel Melati Bandung", "location": "Bandung",
     "rooms": ["Standard", "Deluxe"]},
    {"id": 3, "name": "Hotel Cempaka Jakarta", "location": "Jakarta",
     "rooms": ["Deluxe", "Suite"]},
]

# "Database" riwayat pesanan in-memory, cukup untuk keperluan demo/testing
ORDER_HISTORY = []


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search", methods=["POST"])
def search():
    location = request.form.get("location", "").strip()
    checkin = request.form.get("checkin", "")
    checkout = request.form.get("checkout", "")

    if not location:
        return render_template("home.html", error="Lokasi harus diisi")

    session["search"] = {"location": location, "checkin": checkin, "checkout": checkout}
    results = [h for h in HOTELS if h["location"].lower() == location.lower()]
    return render_template("results.html", hotels=results, location=location)


@app.route("/hotel/<int:hotel_id>")
def hotel_detail(hotel_id):
    hotel = next((h for h in HOTELS if h["id"] == hotel_id), None)
    if not hotel:
        return redirect(url_for("home"))
    session["hotel_id"] = hotel_id
    return render_template("detail.html", hotel=hotel)


@app.route("/select-room", methods=["POST"])
def select_room():
    room_type = request.form.get("room_type")
    session["room_type"] = room_type
    return redirect(url_for("booking_form"))


@app.route("/booking-form", methods=["GET", "POST"])
def booking_form():
    if request.method == "GET":
        return render_template("booking_form.html")

    name = request.form.get("guest_name", "").strip()
    email = request.form.get("guest_email", "").strip()

    if "@" not in email or "." not in email.split("@")[-1]:
        return render_template("booking_form.html", email_error=True,
                                name=name, email=email)

    session["guest_name"] = name
    session["guest_email"] = email
    return redirect(url_for("payment"))


@app.route("/payment", methods=["GET", "POST"])
def payment():
    if request.method == "GET":
        return render_template("payment.html")

    card_number = request.form.get("card_number", "").replace(" ", "")
    cvv = request.form.get("cvv", "")

    if card_number == "" or set(card_number) == {"0"} or len(card_number) < 12:
        return render_template("payment.html", payment_error=True)

    booking_ref = "BKN-" + uuid.uuid4().hex[:8].upper()
    ORDER_HISTORY.append({
        "ref": booking_ref,
        "hotel_id": session.get("hotel_id"),
        "room_type": session.get("room_type"),
        "guest_name": session.get("guest_name"),
    })
    session["booking_ref"] = booking_ref
    return redirect(url_for("confirmation"))


@app.route("/confirmation")
def confirmation():
    ref = session.get("booking_ref", "")
    return render_template("confirmation.html", booking_ref=ref)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["logged_in"] = True
        return redirect(url_for("history"))
    return render_template("login.html")


@app.route("/history")
def history():
    return render_template("history.html", orders=ORDER_HISTORY)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
