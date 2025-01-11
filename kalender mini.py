# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program kalender mini

print('-'*40)
print("\tKALENDER MINI")
print('-'*40)

import calendar

tahun = int(input("Masukkan tahun: "))
bulan = int(input("Masukkan bulan: "))
print(calendar.month(tahun,bulan))