from flask import Flask, render_template, request, redirect
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

app = Flask(__name__)

# Koneksi ke Google Spreadsheet
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Presensi_Siswa").sheet1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/absen', methods=['POST'])
def absen():
    nama = request.form['nama']
    kelas = request.form['kelas']
    status = request.form['status']
    now = datetime.now()
    tanggal = now.strftime("%Y-%m-%d")
    jam = now.strftime("%H:%M:%S")
    lokasi = request.form.get('lokasi', 'Tidak terdeteksi')

    sheet.append_row([nama, kelas, tanggal, jam, status, lokasi])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
