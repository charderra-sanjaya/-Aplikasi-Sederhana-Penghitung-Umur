from typing import Type

import datetime

tanggal = int(input("Masukan Tanggal lahir anda: "))
bulan = int(input("Masukan Bulan lahir anda: "))
tahun = int(input("Masukan Tahun lahir anda: "))

tanggal_lahir = datetime.date(tahun, bulan, tanggal)  # Tanggal lahir
hari_ini = datetime.date.today()  # Hari Ini

# Operasi Hitung Tanggal Lahir dan hari lahirp
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365  # Untuk Umur
umur_bulan_sisa = (umur_hari.days % 365) // 30  # Untuk Bulan sisa

print(5*"=" + "Hasil" + "="*5)
print(f"\nHari Lahir saya Adalah : {tanggal_lahir:%A}")
print(f"Umur Saya adalah : {umur_tahun} tahun, {umur_bulan_sisa} Bulan")
